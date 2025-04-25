from typing import Literal
import reflex as rx
from reflex_experiment.attributes import HTMLProps, HTMLButtonProps
from reflex_experiment.helpers import TypedEventHandler


class HoverCardRoot(HTMLProps):
    """A hover card component based on shadcn/ui."""

    library = "$/custom/shadcn/hover-card"
    tag = "HoverCard"

    # HoverCard specific props
    default_open: rx.Var[bool]
    open: rx.Var[bool]
    on_open_change: TypedEventHandler[bool]
    open_delay: rx.Var[int]
    close_delay: rx.Var[int]


class HoverCardTrigger(HTMLButtonProps):
    """A trigger for a hover card."""

    library = "$/custom/shadcn/hover-card"
    tag = "HoverCardTrigger"

    # HoverCardTrigger specific props
    as_child: rx.Var[bool]


class HoverCardContent(HTMLProps):
    """The content of a hover card."""

    library = "$/custom/shadcn/hover-card"
    tag = "HoverCardContent"

    # HoverCardContent specific props
    force_mount: rx.Var[bool]
    side: rx.Var[Literal["top", "right", "bottom", "left"]]
    side_offset: rx.Var[int]
    align: rx.Var[Literal["start", "center", "end"]]
    align_offset: rx.Var[int]
    avoid_collisions: rx.Var[bool]
    collision_boundary: rx.Var[str]
    collision_padding: rx.Var[int]
    arrow_padding: rx.Var[int]
    sticky: rx.Var[Literal["partial", "always"]]
    hide_when_detached: rx.Var[bool]


class HoverCardNamespace(rx.ComponentNamespace):
    root = staticmethod(HoverCardRoot.create)
    trigger = staticmethod(HoverCardTrigger.create)
    content = staticmethod(HoverCardContent.create)


hover_card = HoverCardNamespace()


__all__ = [
    "HoverCardRoot",
    "HoverCardTrigger",
    "HoverCardContent",
    "hover_card",
    "HoverCardNamespace",
]
