from typing import Literal
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import FormElementMixin, HTMLEventHandlersMixin


class Toggle(rx.Component, FormElementMixin, HTMLEventHandlersMixin):
    """A toggle component based on shadcn/ui."""

    library = "$/custom/shadcn/toggle"
    tag = "Toggle"

    # Toggle specific props
    defaultPressed: rx.Var[bool] = rx.Var.create(False)
    pressed: rx.Var[bool] = rx.Var.create(False)
    onPressedChange: rx.EventHandler[lambda pressed: [pressed]]
    asChild: rx.Var[bool] = rx.Var.create(False)
    variant: rx.Var[Literal["default", "outline"]] = rx.Var.create("default")
    size: rx.Var[Literal["default", "sm", "lg"]] = rx.Var.create("default")


def toggle(*children, **props):
    """Create a Toggle component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Toggle.create(*children, **updated_props)


__all__ = ["Toggle", "toggle"]
