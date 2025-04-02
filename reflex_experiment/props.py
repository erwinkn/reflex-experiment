from typing import Callable, get_type_hints
import reflex as rx
from pydantic.v1.fields import ModelField


def _map_prop_type(type_hint) -> type:
    if type_hint.__name__ in ("Var", "EventHandler", "Annotated"):
        return type_hint
    if type_hint.__name__ == "Callable":
        # In the general case, we have no guarantees the event is serializable (Reflex fails on circular events)
        return rx.EventHandler[lambda: []]
    return rx.Var[type_hint]


def with_props(props_class):
    def decorator(cls: type[rx.Component]):
        hints = get_type_hints(props_class, include_extras=True)
        for field_name, field_type in hints.items():
            if field_name in cls.__fields__:
                continue

            mapped_type = _map_prop_type(field_type)
            if field_name == "on_click":
                print("on_click type:", mapped_type)
            field = ModelField.infer(
                name=field_name,
                value=None,
                annotation=mapped_type,
                class_validators=None,
                config=cls.__config__,
            )
            field.required = False  # Reflex does this for all props
            field = ModelField(
                name=field_name,
                type_=mapped_type,
                class_validators=None,
                model_config=cls.__config__,
                required=False,
            )
            # TODO: check alias
            cls.__fields__[field_name] = field
        cls.get_props.cache_clear()
        return cls

    return decorator
