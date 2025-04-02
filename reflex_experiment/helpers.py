from inspect import isclass
from types import NoneType, UnionType
from typing import (
    Any,
    Literal,
    Type,
    TypeGuard,
    get_args,
    get_origin,
    Union,
    Callable,
)
import reflex as rx
from pydantic.v1 import BaseModel
from pydantic.v1.fields import ModelField
from pydantic.v1.generics import GenericModel
from reflex.vars import (
    ObjectVar,
    Var,
    ArrayVar,
    VarData,
    var_operation,
    var_operation_return,
)
from reflex.utils.imports import ImportVar
from functools import cache


def to_camel(snake_str: str) -> str:
    """Convert snake_case to camelCase, preserving all leading/trailing underscores."""
    # Count and strip leading/trailing underscores
    leading_underscores = len(snake_str) - len(snake_str.lstrip("_"))
    trailing_underscores = len(snake_str) - len(snake_str.rstrip("_"))
    base = snake_str.strip("_")

    if not base:  # Handle string of only underscores
        return snake_str

    # Convert to camel case
    components = base.split("_")
    result = components[0] + "".join(x.title() for x in components[1:])

    # Restore all underscores
    return ("_" * leading_underscores) + result + ("_" * trailing_underscores)


JS_NULL: Var[None] = Var(_js_expr="null", _var_type=None)


def is_pydantic_model(typ) -> TypeGuard[type[BaseModel]]:
    return isclass(typ) and issubclass(typ, BaseModel)


def assert_is_concrete_model(typ):
    if isclass(typ) and issubclass(typ, GenericModel) and not typ.__concrete__:
        raise ValueError("Non-concrete generic Pydantic models are not supported")


PRIMITIVE_TYPES = (int, float, str, bool, NoneType)


@cache
def _create_value_converter(type_: Type) -> Callable[[Var], Var]:
    """Creates a lambda to convert a Var based on the target Python type."""
    if type_ in PRIMITIVE_TYPES:
        return lambda var: var  # Primitive types pass through

    if is_pydantic_model(type_):
        assert_is_concrete_model(type_)
        return _create_model_converter(type_)

    origin = get_origin(type_)
    args = get_args(type_)

    if origin is Literal:
        assert all(type(arg) in PRIMITIVE_TYPES for arg in args), (
            f"Only primitive values ({PRIMITIVE_TYPES}) are supported in literals, received {type_}"
        )
        return lambda var: var

    # Non-discriminated Unions of primitives
    if origin is Union or origin is UnionType:
        assert all(type(arg) in PRIMITIVE_TYPES for arg in args), (
            f"Only primitive values ({PRIMITIVE_TYPES}) are supported in unions, received {type_}"
        )
        return lambda var: var  # Pass through if only primitives

    if origin is tuple:
        element_converters = [_create_value_converter(arg) for arg in args]
        return lambda var: Var.create(
            [
                converter(var.to(ArrayVar)[i])
                for i, converter in enumerate(element_converters)
            ]
        )

    if origin is list:
        element_converter = _create_value_converter(args[0])
        return lambda var: var.to(ArrayVar).foreach(element_converter)

    if origin is dict:
        assert args[0] is str, "Only string keys are allowed for dictionaries"
        assert args[1] in (int, float, str), (
            "Only primitive types are currently supported for dictionary values"
        )
        # For primitive dict values, no complex conversion needed per item
        return lambda var: var

    raise ValueError(
        f"Unsupported field type: {type_} (origin: {origin}, args: {args})"
    )


@cache
def _create_field_converter(field: ModelField) -> Callable[[Var], Var]:
    """Creates a lambda to convert a Var for a specific Pydantic field."""
    # Handle discriminated union first
    if field.discriminator_key is not None:
        if not field.sub_fields_mapping:
            # This can happen if forward refs aren't resolved, though less likely in this context.
            # Handle appropriately, maybe raise an error earlier.
            raise TypeError(
                f"Discriminated union field '{field.name}' sub_fields_mapping is not populated."
            )

        # Get the JS name (alias) of the discriminator field itself.
        # Pydantic ensures this alias exists and is unique across sub-models.
        discriminator_alias = field.discriminator_alias
        if discriminator_alias is None:
            # Should ideally not happen if discriminator_key is set, but safety first.
            raise ValueError(
                f"Cannot determine discriminator alias for field '{field.name}'"
            )

        # Pre-calculate converters for each sub-model
        sub_model_converters = {
            literal: _create_model_converter(sub_field.type_)
            for literal, sub_field in field.sub_fields_mapping.items()
        }
        camel_discriminator_alias = to_camel(discriminator_alias)

        def discriminated_union_converter(var: Var) -> Var:
            obj_var = var.to(ObjectVar)  # Ensure we have an object var
            discriminator_value_var = getattr(obj_var, camel_discriminator_alias)
            cases = [
                (
                    literal,
                    converter(obj_var),
                )  # Apply the sub-converter to the whole object
                for literal, converter in sub_model_converters.items()
            ]
            return rx.match(discriminator_value_var, *cases, JS_NULL).to(ObjectVar)

        value_converter = discriminated_union_converter

    else:
        # Create the main value converter for the field's type
        value_converter = _create_value_converter(field.outer_type_)

    if not field.required:

        def optional_converter(var: Var) -> Var:
            return rx.cond(var == rx.Var.create(None), JS_NULL, value_converter(var))

        return optional_converter
    else:
        # If required, just use the value converter directly
        return value_converter


@cache
def _create_model_converter(model: type[BaseModel]) -> Callable[[Var], Var]:
    """Creates a lambda to convert a Var to a dict structure matching the Pydantic model."""

    assert_is_concrete_model(model)
    # Pre-calculate field converters and their JS camelCase names (using alias)
    field_converters = {
        field_name: (to_camel(field.alias), _create_field_converter(field))
        for field_name, field in model.__fields__.items()
    }

    def model_converter(var: Var) -> Var:
        obj_var = var.to(ObjectVar)  # Ensure we have an object var
        result_dict = {}
        for field_name, (camel_alias, converter) in field_converters.items():
            field_var = getattr(obj_var, camel_alias)
            result_dict[field_name] = converter(field_var)
        return Var.create(result_dict)

    return model_converter


# Updated create_event_handler
# No longer uses create_camel_model
@cache
def create_event_handler(event, element):
    """
    Creates an event handler that automatically converts a JS event object (camelCase)
    to a specified Pydantic model instance (snake_case) wrapped in a Reflex Var.
    """
    event_model: type[BaseModel] = event[element]

    # Get the cached converter lambda for this specific concrete model type
    converter_lambda = _create_model_converter(event_model)

    def handler(evt: ObjectVar) -> tuple[event_model]:  # type: ignore
        """
        The generated event handler function.

        Args:
            evt: The raw Javascript event object Var (assumed to have camelCase properties).

        Returns:
            A tuple containing a single Reflex Var mapped to the concrete_event model.
        """
        # Apply the cached converter lambda
        converted_var = converter_lambda(evt)
        # Cast the result to the specific Pydantic model type
        result = converted_var.to(event_model)
        return (result,)

    return handler
