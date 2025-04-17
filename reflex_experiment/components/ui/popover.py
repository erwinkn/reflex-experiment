from typing import Literal
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import GlobalAttributes, HTMLEventHandlersMixin


class Popover(rx.Component, GlobalAttributes):
    """A popover component based on shadcn/ui."""

    library = "$/custom/shadcn/popover"
    tag = "Popover"

    # Popover specific props
    defaultOpen: rx.Var[bool] = rx.Var.create(False)
    open: rx.Var[bool] = rx.Var.create(False)
    onOpenChange: rx.EventHandler[lambda open: [open]]
    modal: rx.Var[bool] = rx.Var.create(False)


class PopoverTrigger(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A trigger for a popover."""

    library = "$/custom/shadcn/popover"
    tag = "PopoverTrigger"

    # PopoverTrigger specific props
    asChild: rx.Var[bool] = rx.Var.create(False)


class PopoverContent(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The content of a popover."""

    library = "$/custom/shadcn/popover"
    tag = "PopoverContent"

    # PopoverContent specific props
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
    updatePositionStrategy: rx.Var[Literal["optimized", "always"]] = rx.Var.create(
        "optimized"
    )
    onEscapeKeyDown: rx.EventHandler[lambda event: [event]]
    onPointerDownOutside: rx.EventHandler[lambda event: [event]]
    onFocusOutside: rx.EventHandler[lambda event: [event]]
    onInteractOutside: rx.EventHandler[lambda event: [event]]


# Create helper functions


def popover(*children, **props):
    """Create a Popover component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Popover.create(*children, **updated_props)


def popover_trigger(*children, **props):
    """Create a PopoverTrigger component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return PopoverTrigger.create(*children, **updated_props)


def popover_content(*children, **props):
    """Create a PopoverContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return PopoverContent.create(*children, **updated_props)


__all__ = [
    "Popover",
    "popover",
    "PopoverTrigger",
    "popover_trigger",
    "PopoverContent",
    "popover_content",
]
