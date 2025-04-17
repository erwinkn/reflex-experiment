from typing import Literal
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import ButtonHTMLAttributes, HTMLAttributes


class Drawer(rx.Component):
    """A drawer component based on shadcn/ui."""

    library = "$/custom/shadcn/drawer"
    tag = "Drawer"
    lib_dependencies = ["vaul"]

    # Drawer specific props
    open: rx.Var[bool]
    on_open_change: rx.EventHandler[lambda open: [open]]
    on_drag: rx.EventHandler[lambda evt: [evt]]
    on_release: rx.EventHandler[lambda evt: [evt]]
    snap_points: rx.Var[list[float | str]]
    should_scale_background: rx.Var[bool]
    set_background_color_on_scale: rx.Var[bool]
    close_threshold: rx.Var[float]
    scroll_lock_timeout: rx.Var[float]
    dismissible: rx.Var[bool]
    handle_only: rx.Var[bool]
    fade_from_index: rx.Var[int]
    active_snap_point: rx.Var[int | str]
    set_active_snap_point: rx.EventHandler[lambda idx: [idx]]
    fixed: rx.Var[bool]
    modal: rx.Var[bool]
    on_close: rx.EventHandler
    nested: rx.Var[bool]
    no_body_styles: rx.Var[bool]
    direction: rx.Var[Literal["top", "right", "bottom", "left"]]
    default_open: rx.Var[bool]
    disable_prevent_scroll: rx.Var[bool]
    snap_to_sequential_point: rx.Var[bool]
    prevent_scroll_restoration: rx.Var[bool]
    reposition_inputs: rx.Var[bool]
    on_animation_end: rx.EventHandler[lambda open: None]
    # TODO: container
    auto_focus: rx.Var[bool]


class DrawerTrigger(rx.Component, ButtonHTMLAttributes):
    """The trigger button for a drawer."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerTrigger"

    # DrawerTrigger specific props
    as_child: rx.Var[bool]


class DrawerClose(rx.Component, ButtonHTMLAttributes):
    """A button to close the drawer."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerClose"

    # DrawerClose specific props
    as_child: rx.Var[bool]


class DrawerPortal(rx.Component, HTMLAttributes):
    """A portal for the drawer content."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerPortal"


class DrawerOverlay(rx.Component, HTMLAttributes):
    """The overlay for the drawer."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerOverlay"

    as_child: rx.Var[bool]


class DrawerContent(rx.Component, HTMLAttributes):
    """The content of the drawer."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerContent"

    # DrawerContent specific props
    as_child: rx.Var[bool]


class DrawerHeader(rx.Component, HTMLAttributes):
    """The header of the drawer."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerHeader"


class DrawerBody(rx.Component, HTMLAttributes):
    """The body of the drawer."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerBody"

    as_child: rx.Var[bool]


class DrawerFooter(rx.Component, HTMLAttributes):
    """The footer of the drawer."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerFooter"


class DrawerTitle(rx.Component, HTMLAttributes):
    """The title of the drawer."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerTitle"

    # DrawerTitle specific props
    as_child: rx.Var[bool]


class DrawerDescription(rx.Component, HTMLAttributes):
    """The description of the drawer."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerDescription"

    # DrawerDescription specific props
    as_child: rx.Var[bool]


# Create helper functions


def drawer(*children, **props):
    """Create a Drawer component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Drawer.create(*children, **updated_props)


def drawer_trigger(*children, **props):
    """Create a DrawerTrigger component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DrawerTrigger.create(*children, **updated_props)


def drawer_close(*children, **props):
    """Create a DrawerClose component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DrawerClose.create(*children, **updated_props)


def drawer_portal(*children, **props):
    """Create a DrawerPortal component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DrawerPortal.create(*children, **updated_props)


def drawer_overlay(*children, **props):
    """Create a DrawerOverlay component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DrawerOverlay.create(*children, **updated_props)


def drawer_content(*children, **props):
    """Create a DrawerContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DrawerContent.create(*children, **updated_props)


def drawer_header(*children, **props):
    """Create a DrawerHeader component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DrawerHeader.create(*children, **updated_props)


def drawer_body(*children, **props):
    """Create a DrawerBody component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DrawerBody.create(*children, **updated_props)


def drawer_footer(*children, **props):
    """Create a DrawerFooter component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DrawerFooter.create(*children, **updated_props)


def drawer_title(*children, **props):
    """Create a DrawerTitle component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DrawerTitle.create(*children, **updated_props)


def drawer_description(*children, **props):
    """Create a DrawerDescription component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DrawerDescription.create(*children, **updated_props)


__all__ = [
    "Drawer",
    "drawer",
    "DrawerTrigger",
    "drawer_trigger",
    "DrawerClose",
    "drawer_close",
    "DrawerPortal",
    "drawer_portal",
    "DrawerOverlay",
    "drawer_overlay",
    "DrawerContent",
    "drawer_content",
    "DrawerHeader",
    "drawer_header",
    "DrawerBody",
    "drawer_body",
    "DrawerFooter",
    "drawer_footer",
    "DrawerTitle",
    "drawer_title",
    "DrawerDescription",
    "drawer_description",
]
