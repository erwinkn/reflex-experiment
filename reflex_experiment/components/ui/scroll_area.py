from typing import Literal
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import GlobalAttributes, HTMLEventHandlersMixin


class ScrollArea(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A scroll area component based on shadcn/ui."""

    library = "$/custom/shadcn/scroll-area"
    tag = "ScrollArea"

    # ScrollArea specific props
    type: rx.Var[Literal["auto", "always", "scroll", "hover"]] = rx.Var.create("auto")
    scrollHideDelay: rx.Var[int] = rx.Var.create(600)
    asChild: rx.Var[bool] = rx.Var.create(False)


class ScrollBar(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A scroll bar within a scroll area."""

    library = "$/custom/shadcn/scroll-area"
    tag = "ScrollBar"

    # ScrollBar specific props
    orientation: rx.Var[Literal["horizontal", "vertical"]] = rx.Var.create("vertical")
    forceMount: rx.Var[bool] = rx.Var.create(False)


# Create helper functions


def scroll_area(*children, **props):
    """Create a ScrollArea component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ScrollArea.create(*children, **updated_props)


def scroll_bar(*children, **props):
    """Create a ScrollBar component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ScrollBar.create(*children, **updated_props)


__all__ = [
    "ScrollArea",
    "scroll_area",
    "ScrollBar",
    "scroll_bar",
]
