from typing import Literal
import reflex as rx
from reflex_experiment.attributes import HTMLProps, HTMLButtonProps
from reflex_experiment.components.ui.dropdown_menu import Padding
from reflex_experiment.elements import HTMLElement
from reflex_experiment.events import (
    FocusEvent,
    KeyboardEvent,
    PointerEvent,
    SyntheticEvent,
)
from reflex_experiment.helpers import TypedEventHandler


class PopoverRoot(HTMLProps):
    """A popover component based on shadcn/ui."""

    library = "$/custom/shadcn/popover"
    tag = "Popover"

    # Popover specific props
    default_open: rx.Var[bool]
    open: rx.Var[bool]
    # (open: boolean) => void
    on_open_change: TypedEventHandler[bool]
    modal: rx.Var[bool]


class PopoverTrigger(HTMLButtonProps):
    """A trigger for a popover."""

    library = "$/custom/shadcn/popover"
    tag = "PopoverTrigger"

    # PopoverTrigger specific props
    as_child: rx.Var[bool]


class PopoverContent(HTMLProps):
    """The content of a popover."""

    library = "$/custom/shadcn/popover"
    tag = "PopoverContent"

    # PopoverContent specific props
    force_mount: rx.Var[bool]
    side: rx.Var[Literal["top", "right", "bottom", "left"]]
    side_offset: rx.Var[int]
    align: rx.Var[Literal["start", "center", "end"]]
    align_offset: rx.Var[int]
    avoid_collisions: rx.Var[bool]
    # Have to pass in elements
    # collision_boundary: rx.Var[str]
    collision_padding: rx.Var[int | Padding]
    arrow_padding: rx.Var[int]
    sticky: rx.Var[Literal["partial", "always"]]
    hide_when_detached: rx.Var[bool]
    on_open_auto_focus: TypedEventHandler[SyntheticEvent[HTMLElement]]
    on_close_auto_focus: TypedEventHandler[SyntheticEvent[HTMLElement]]
    on_escape_key_down: TypedEventHandler[KeyboardEvent[HTMLElement]]
    on_pointer_down_outside: TypedEventHandler[PointerEvent[HTMLElement]]
    on_focus_outside: TypedEventHandler[FocusEvent[HTMLElement]]
    # Actually this is PointerEvent | FocusEvent, but not sure the
    # serializer/deserializer can handle this kind of union.
    # If you want the specific event, use on_pointer_down_outside and
    # on_focus_outside.
    on_interact_outside: TypedEventHandler[SyntheticEvent[HTMLElement]]


class PopoverNamespace(rx.ComponentNamespace):
    root = staticmethod(PopoverRoot.create)
    trigger = staticmethod(PopoverTrigger.create)
    content = staticmethod(PopoverContent.create)


popover = PopoverNamespace()


__all__ = [
    "PopoverRoot",
    "PopoverTrigger",
    "PopoverContent",
    "popover",
    "PopoverNamespace",
]
