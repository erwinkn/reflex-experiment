from typing import Type
from pydantic.v1 import BaseModel, create_model


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


def create_camel_model(
    model: Type[BaseModel], suffix: str = "Native"
) -> Type[BaseModel]:
    """Creates a new Pydantic model with camelCase field names."""
    fields = {}
    for name, field in model.__fields__.items():
        camel_name = to_camel(name)
        fields[camel_name] = (field.type_, field.field_info)

    return create_model(f"{model.__name__}{suffix}", __base__=BaseModel, **fields)
