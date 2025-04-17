from typing import Literal
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import GlobalAttributes, HTMLEventHandlersMixin


class Tooltip(rx.Component, GlobalAttributes):
    """A tooltip component based on shadcn/ui."""

    library = "$/custom/shadcn/tooltip"
    tag = "Tooltip"

    # Tooltip specific props
    defaultOpen: rx.Var[bool] = rx.Var.create(False)
    open: rx.Var[bool] = rx.Var.create(False)
    onOpenChange: rx.EventHandler[lambda open: [open]]
    delayDuration: rx.Var[int] = rx.Var.create(700)
    disableHoverableContent: rx.Var[bool] = rx.Var.create(False)


class TooltipTrigger(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The trigger for a tooltip."""

    library = "$/custom/shadcn/tooltip"
    tag = "TooltipTrigger"

    # TooltipTrigger specific props
    asChild: rx.Var[bool] = rx.Var.create(False)


class TooltipContent(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The content of a tooltip."""

    library = "$/custom/shadcn/tooltip"
    tag = "TooltipContent"

    # TooltipContent specific props
    side: rx.Var[Literal["top", "right", "bottom", "left"]] = rx.Var.create("top")
    sideOffset: rx.Var[int] = rx.Var.create(4)
    align: rx.Var[Literal["start", "center", "end"]] = rx.Var.create("center")
    alignOffset: rx.Var[int] = rx.Var.create(0)
    avoidCollisions: rx.Var[bool] = rx.Var.create(True)
    sticky: rx.Var[Literal["partial", "always"]] = rx.Var.create("partial")
    hideWhenDetached: rx.Var[bool] = rx.Var.create(False)


# Create helper functions


def tooltip(*children, **props):
    """Create a Tooltip component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Tooltip.create(*children, **updated_props)


def tooltip_trigger(*children, **props):
    """Create a TooltipTrigger component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return TooltipTrigger.create(*children, **updated_props)


def tooltip_content(*children, **props):
    """Create a TooltipContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return TooltipContent.create(*children, **updated_props)


__all__ = [
    "Tooltip",
    "tooltip",
    "TooltipTrigger",
    "tooltip_trigger",
    "TooltipContent",
    "tooltip_content",
]
