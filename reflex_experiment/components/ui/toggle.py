from typing import Literal
import reflex as rx
from reflex_experiment.attributes import HTMLButtonProps
from reflex_experiment.helpers import TypedEventHandler


class Toggle(HTMLButtonProps):
    """A toggle component based on shadcn/ui."""

    library = "$/custom/shadcn/toggle"
    tag = "Toggle"

    # Toggle specific props
    default_pressed: rx.Var[bool]
    pressed: rx.Var[bool]
    on_pressed_change: TypedEventHandler[bool]
    as_child: rx.Var[bool]
    variant: rx.Var[Literal["default", "outline"]]
    size: rx.Var[Literal["default", "sm", "lg"]]


toggle = Toggle.create


__all__ = ["toggle", "Toggle"]
