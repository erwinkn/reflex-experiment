from typing import Literal, List
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import GlobalAttributes, HTMLEventHandlersMixin


class ToggleGroup(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A toggle group component based on shadcn/ui."""

    library = "$/custom/shadcn/toggle-group"
    tag = "ToggleGroup"

    # ToggleGroup specific props
    type: rx.Var[Literal["single", "multiple"]] = rx.Var.create("single")
    defaultValue: rx.Var[str] = rx.Var.create("")
    value: rx.Var[str] = rx.Var.create("")
    onValueChange: rx.EventHandler[lambda value: [value]]
    disabled: rx.Var[bool] = rx.Var.create(False)
    variant: rx.Var[Literal["default", "outline"]] = rx.Var.create("default")
    size: rx.Var[Literal["default", "sm", "lg"]] = rx.Var.create("default")
    orientation: rx.Var[Literal["horizontal", "vertical"]] = rx.Var.create("horizontal")
    loop: rx.Var[bool] = rx.Var.create(True)
    rovingFocus: rx.Var[bool] = rx.Var.create(True)


class ToggleGroupItem(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """An item in a toggle group component."""

    library = "$/custom/shadcn/toggle-group"
    tag = "ToggleGroupItem"

    # ToggleGroupItem specific props
    value: rx.Var[str] = rx.Var.create("")
    disabled: rx.Var[bool] = rx.Var.create(False)
    asChild: rx.Var[bool] = rx.Var.create(False)


# Create helper functions


def toggle_group(*children, **props):
    """Create a ToggleGroup component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ToggleGroup.create(*children, **updated_props)


def toggle_group_item(*children, **props):
    """Create a ToggleGroupItem component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ToggleGroupItem.create(*children, **updated_props)


__all__ = [
    "ToggleGroup",
    "toggle_group",
    "ToggleGroupItem",
    "toggle_group_item",
]
