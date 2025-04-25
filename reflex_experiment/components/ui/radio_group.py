from typing import Literal
import reflex as rx
from reflex_experiment.attributes import HTMLButtonProps, HTMLProps
from reflex_experiment.helpers import TypedEventHandler


class RadioGroupRoot(HTMLProps):
    """A radio group component based on shadcn/ui."""

    library = "$/custom/shadcn/radio-group"
    tag = "RadioGroup"

    # RadioGroup specific props
    default_value: rx.Var[str]
    on_value_change: TypedEventHandler[str]
    loop: rx.Var[bool]
    orientation: rx.Var[Literal["horizontal", "vertical"]]


class RadioGroupItem(HTMLButtonProps):
    """A radio button in a radio group component."""

    library = "$/custom/shadcn/radio-group"
    tag = "RadioGroupItem"

    # RadioGroupItem specific props
    value: rx.Var[str]
    disabled: rx.Var[bool]
    required: rx.Var[bool]
    as_child: rx.Var[bool]


class RadioGroupNamespace(rx.ComponentNamespace):
    root = staticmethod(RadioGroupRoot.create)
    item = staticmethod(RadioGroupItem.create)


radio_group = RadioGroupNamespace()


__all__ = [
    "RadioGroupRoot",
    "RadioGroupItem",
    "radio_group",
    "RadioGroupNamespace",
]
