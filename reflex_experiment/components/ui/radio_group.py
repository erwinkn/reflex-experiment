from typing import Literal
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import FormElementMixin, GlobalAttributes, HTMLEventHandlersMixin


class RadioGroup(rx.Component, FormElementMixin, HTMLEventHandlersMixin):
    """A radio group component based on shadcn/ui."""

    library = "$/custom/shadcn/radio-group"
    tag = "RadioGroup"

    # RadioGroup specific props
    defaultValue: rx.Var[str] = rx.Var.create("")
    onValueChange: rx.EventHandler[lambda value: [value]]
    loop: rx.Var[bool] = rx.Var.create(True)
    orientation: rx.Var[Literal["horizontal", "vertical"]] = rx.Var.create("vertical")


class RadioGroupItem(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A radio button in a radio group component."""

    library = "$/custom/shadcn/radio-group"
    tag = "RadioGroupItem"

    # RadioGroupItem specific props
    value: rx.Var[str] = rx.Var.create("")
    disabled: rx.Var[bool] = rx.Var.create(False)
    required: rx.Var[bool] = rx.Var.create(False)
    asChild: rx.Var[bool] = rx.Var.create(False)


# Create helper functions


def radio_group(*children, **props):
    """Create a RadioGroup component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return RadioGroup.create(*children, **updated_props)


def radio_group_item(*children, **props):
    """Create a RadioGroupItem component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return RadioGroupItem.create(*children, **updated_props)


__all__ = [
    "RadioGroup",
    "radio_group",
    "RadioGroupItem",
    "radio_group_item",
]
