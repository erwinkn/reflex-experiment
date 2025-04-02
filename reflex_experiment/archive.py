from typing import (
    Type,
    get_args,
    get_origin,
)
from pydantic.v1 import BaseModel, create_model
from pydantic.v1.fields import FieldInfo
from functools import cache

from reflex_experiment.helpers import to_camel


@cache
def create_camel_model(
    model: Type[BaseModel], suffix: str = "", prefix: str = "", use_alias=False
) -> Type[BaseModel]:
    """Creates a new Pydantic model with camelCase field names."""
    if not prefix and not suffix:
        raise ValueError("Please provide at least a suffix or prefix")
    fields = {}
    for field_name, field in model.__fields__.items():
        field_camel_name = to_camel(field.alias if use_alias else field_name)
        field_type = field.type_
        field_info = field.field_info

        # Handle nested models and collections of models
        origin = get_origin(field_type)
        if origin is not None:
            args = get_args(field_type)
            if any(
                isinstance(arg, type) and issubclass(arg, BaseModel) for arg in args
            ):
                # Handle List[Model], Optional[Model], etc.
                new_args = tuple(
                    create_camel_model(arg, prefix=prefix, suffix=suffix)
                    if isinstance(arg, type) and issubclass(arg, BaseModel)
                    else arg
                    for arg in args
                )
                field_type = origin[new_args]
        elif isinstance(field_type, type) and issubclass(field_type, BaseModel):
            # Handle nested model
            field_type = create_camel_model(field_type, prefix=prefix, suffix=suffix)

        field_alias = (
            field.alias if field.has_alias and field.alias != field_camel_name else None
        )
        mapped_field_info = FieldInfo(
            **{key: getattr(field_info, key) for key in field_info.get_constraints()},
            alias=field_alias,
            alias_priority=field_info.alias_priority if field_alias else None,
            # we don't handle regex updates as that wouldn't be realistic
            discriminator=to_camel(field_info.discriminator)
            if field_info.discriminator is not None
            else None,
        )
        fields[field_camel_name] = (field_type, mapped_field_info)

    return create_model(
        f"{prefix}{model.__name__}{suffix}", __base__=BaseModel, **fields
    )
