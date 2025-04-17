from typing import Literal
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import GlobalAttributes, HTMLEventHandlersMixin


class HoverCard(rx.Component, GlobalAttributes):
    """A hover card component based on shadcn/ui."""

    library = "$/custom/shadcn/hover-card"
    tag = "HoverCard"

    # HoverCard specific props
    defaultOpen: rx.Var[bool] = rx.Var.create(False)
    open: rx.Var[bool] = rx.Var.create(False)
    onOpenChange: rx.EventHandler[lambda open: [open]]
    openDelay: rx.Var[int] = rx.Var.create(700)
    closeDelay: rx.Var[int] = rx.Var.create(300)


class HoverCardTrigger(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A trigger for a hover card."""

    library = "$/custom/shadcn/hover-card"
    tag = "HoverCardTrigger"

    # HoverCardTrigger specific props
    asChild: rx.Var[bool] = rx.Var.create(False)


class HoverCardContent(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The content of a hover card."""

    library = "$/custom/shadcn/hover-card"
    tag = "HoverCardContent"

    # HoverCardContent specific props
    forceMount: rx.Var[bool] = rx.Var.create(False)
    side: rx.Var[Literal["top", "right", "bottom", "left"]] = rx.Var.create("bottom")
    sideOffset: rx.Var[int] = rx.Var.create(4)
    align: rx.Var[Literal["start", "center", "end"]] = rx.Var.create("center")
    alignOffset: rx.Var[int] = rx.Var.create(0)
    avoidCollisions: rx.Var[bool] = rx.Var.create(True)
    collisionBoundary: rx.Var[str] = rx.Var.create("")
    collisionPadding: rx.Var[int] = rx.Var.create(0)
    arrowPadding: rx.Var[int] = rx.Var.create(0)
    sticky: rx.Var[Literal["partial", "always"]] = rx.Var.create("partial")
    hideWhenDetached: rx.Var[bool] = rx.Var.create(False)


# Create helper functions


def hover_card(*children, **props):
    """Create a HoverCard component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return HoverCard.create(*children, **updated_props)


def hover_card_trigger(*children, **props):
    """Create a HoverCardTrigger component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return HoverCardTrigger.create(*children, **updated_props)


def hover_card_content(*children, **props):
    """Create a HoverCardContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return HoverCardContent.create(*children, **updated_props)


__all__ = [
    "HoverCard",
    "hover_card",
    "HoverCardTrigger",
    "hover_card_trigger",
    "HoverCardContent",
    "hover_card_content",
]
