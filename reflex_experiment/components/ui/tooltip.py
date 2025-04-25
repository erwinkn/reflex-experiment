from typing import Literal
import reflex as rx
from reflex_experiment.attributes import HTMLButtonProps, HTMLProps
from reflex_experiment.helpers import TypedEventHandler


class TooltipRoot(HTMLProps):
    """A tooltip component based on shadcn/ui."""

    library = "$/custom/shadcn/tooltip"
    tag = "Tooltip"

    # Tooltip specific props
    default_open: rx.Var[bool]
    open: rx.Var[bool]
    on_open_change: TypedEventHandler[bool]
    delay_duration: rx.Var[int]
    disable_hoverable_content: rx.Var[bool]


class TooltipTrigger(HTMLButtonProps):
    """The trigger for a tooltip."""

    library = "$/custom/shadcn/tooltip"
    tag = "TooltipTrigger"

    # TooltipTrigger specific props
    as_child: rx.Var[bool]


class TooltipContent(HTMLProps):
    """The content of a tooltip."""

    library = "$/custom/shadcn/tooltip"
    tag = "TooltipContent"

    # TooltipContent specific props
    side: rx.Var[Literal["top", "right", "bottom", "left"]]
    side_offset: rx.Var[int]
    align: rx.Var[Literal["start", "center", "end"]]
    align_offset: rx.Var[int]
    avoid_collisions: rx.Var[bool]
    sticky: rx.Var[Literal["partial", "always"]]
    hide_when_detached: rx.Var[bool]


class TooltipNamespace(rx.ComponentNamespace):
    root = staticmethod(TooltipRoot.create)
    trigger = staticmethod(TooltipTrigger.create)
    content = staticmethod(TooltipContent.create)


tooltip = TooltipNamespace()


__all__ = [
    "TooltipRoot",
    "TooltipTrigger",
    "TooltipContent",
    "tooltip",
    "TooltipNamespace",
]
