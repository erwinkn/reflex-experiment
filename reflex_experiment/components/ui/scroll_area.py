from typing import Literal
import reflex as rx
from reflex_experiment.attributes import HTMLProps


class ScrollAreaRoot(HTMLProps):
    """A scroll area component based on shadcn/ui."""

    library = "$/custom/shadcn/scroll-area"
    tag = "ScrollArea"

    # ScrollArea specific props
    type: rx.Var[Literal["auto", "always", "scroll", "hover"]]
    scroll_hide_delay: rx.Var[int]
    as_child: rx.Var[bool]


class ScrollBar(HTMLProps):
    """A scroll bar within a scroll area."""

    library = "$/custom/shadcn/scroll-area"
    tag = "ScrollBar"

    # ScrollBar specific props
    orientation: rx.Var[Literal["horizontal", "vertical"]]
    force_mount: rx.Var[bool]


class ScrollAreaNamespace(rx.ComponentNamespace):
    root = staticmethod(ScrollAreaRoot.create)
    scrollbar = staticmethod(ScrollBar.create)


scroll_area = ScrollAreaNamespace()


__all__ = [
    "ScrollAreaRoot",
    "ScrollBar",
    "scroll_area",
    "ScrollAreaNamespace",
]
