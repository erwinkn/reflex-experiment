import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import ButtonHTMLAttributes, HTMLAttributes


class Collapsible(rx.Component, HTMLAttributes):
    """A collapsible component that can be opened and closed."""

    library = "$/custom/shadcn/collapsible"
    tag = "Collapsible"

    # Collapsible specific props
    as_child: rx.Var[bool]
    default_open: rx.Var[bool]
    open: rx.Var[bool]
    on_open_change: rx.EventHandler[lambda open: [open]]
    disabled: rx.Var[bool]


class CollapsibleTrigger(rx.Component, ButtonHTMLAttributes):
    """A button that triggers the collapsible component to open or close."""

    library = "$/custom/shadcn/collapsible"
    tag = "CollapsibleTrigger"

    # CollapsibleTrigger specific props
    as_child: rx.Var[bool]


class CollapsibleContent(rx.Component, HTMLAttributes):
    """The content of the collapsible component that gets shown or hidden."""

    library = "$/custom/shadcn/collapsible"
    tag = "CollapsibleContent"

    # CollapsibleContent specific props
    as_child: rx.Var[bool]
    force_mount: rx.Var[bool]


# Create helper functions


def collapsible(*children, **props):
    """Create a Collapsible component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Collapsible.create(*children, **updated_props)


def collapsible_trigger(*children, **props):
    """Create a CollapsibleTrigger component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return CollapsibleTrigger.create(*children, **updated_props)


def collapsible_content(*children, **props):
    """Create a CollapsibleContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return CollapsibleContent.create(*children, **updated_props)


__all__ = [
    "Collapsible",
    "collapsible",
    "CollapsibleTrigger",
    "collapsible_trigger",
    "CollapsibleContent",
    "collapsible_content",
]
