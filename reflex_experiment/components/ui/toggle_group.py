from typing import Literal, List
import reflex as rx
from reflex_experiment.attributes import HTMLProps
from reflex_experiment.helpers import TypedEventHandler


class ToggleGroupRoot(HTMLProps):
    """A toggle group component based on shadcn/ui."""

    library = "$/custom/shadcn/toggle-group"
    tag = "ToggleGroup"

    # ToggleGroup specific props
    type: rx.Var[Literal["single", "multiple"]]
    default_value: rx.Var[str | list[str]]
    value: rx.Var[str | list[str]]
    on_value_change: TypedEventHandler[str | list[str]]
    disabled: rx.Var[bool]
    variant: rx.Var[Literal["default", "outline"]]
    size: rx.Var[Literal["default", "sm", "lg"]]
    orientation: rx.Var[Literal["horizontal", "vertical"]]
    loop: rx.Var[bool]
    roving_focus: rx.Var[bool]


class ToggleGroupItem(HTMLProps):
    """An item in a toggle group component."""

    library = "$/custom/shadcn/toggle-group"
    tag = "ToggleGroupItem"

    # ToggleGroupItem specific props
    value: rx.Var[str]
    disabled: rx.Var[bool]
    as_child: rx.Var[bool]


class ToggleGroupNamespace(rx.ComponentNamespace):
    root = staticmethod(ToggleGroupRoot.create)
    item = staticmethod(ToggleGroupItem.create)


toggle_group = ToggleGroupNamespace()


__all__ = [
    "ToggleGroupRoot",
    "ToggleGroupItem",
    "toggle_group",
    "ToggleGroupNamespace",
]
