from typing import Literal, Union
import reflex as rx
from reflex_experiment.attributes import HTMLProps, HTMLButtonProps
from reflex_experiment.elements import HTMLDivElement
from reflex_experiment.events import PointerEvent
from reflex_experiment.helpers import TypedEventHandler


class DrawerRoot(HTMLProps):
    """A drawer component based on shadcn/ui."""

    library = "$/custom/shadcn/drawer"
    tag = "Drawer"
    lib_dependencies = ["vaul"]

    # Drawer specific props
    open: rx.Var[bool]
    on_open_change: TypedEventHandler[bool]
    on_drag: TypedEventHandler[PointerEvent[HTMLDivElement]]
    on_release: TypedEventHandler[PointerEvent[HTMLDivElement]]
    snap_points: rx.Var[list[Union[float, str]]]
    should_scale_background: rx.Var[bool]
    set_background_color_on_scale: rx.Var[bool]
    close_threshold: rx.Var[float]
    scroll_lock_timeout: rx.Var[float]
    dismissible: rx.Var[bool]
    handle_only: rx.Var[bool]
    fade_from_index: rx.Var[int]
    active_snap_point: rx.Var[Union[int, str, None]]
    set_active_snap_point: TypedEventHandler[Union[int, str, None]]
    fixed: rx.Var[bool]
    modal: rx.Var[bool]
    on_close: TypedEventHandler[None]
    nested: rx.Var[bool]
    no_body_styles: rx.Var[bool]
    direction: rx.Var[Literal["top", "right", "bottom", "left"]]
    default_open: rx.Var[bool]
    disable_prevent_scroll: rx.Var[bool]
    snap_to_sequential_point: rx.Var[bool]
    prevent_scroll_restoration: rx.Var[bool]
    reposition_inputs: rx.Var[bool]
    on_animation_end: TypedEventHandler[bool]
    auto_focus: rx.Var[bool]
    # TODO: container


class DrawerTrigger(HTMLButtonProps):
    """The trigger button for a drawer."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerTrigger"

    # DrawerTrigger specific props
    as_child: rx.Var[bool]


class DrawerClose(HTMLButtonProps):
    """A button to close the drawer."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerClose"

    # DrawerClose specific props
    as_child: rx.Var[bool]


class DrawerPortal(HTMLProps):
    """A portal for the drawer content."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerPortal"


class DrawerOverlay(HTMLProps):
    """The overlay for the drawer."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerOverlay"

    as_child: rx.Var[bool]


class DrawerContent(HTMLProps):
    """The content of the drawer."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerContent"

    # DrawerContent specific props
    as_child: rx.Var[bool]


class DrawerHeader(HTMLProps):
    """The header of the drawer."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerHeader"


class DrawerBody(HTMLProps):
    """The body of the drawer."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerBody"

    as_child: rx.Var[bool]


class DrawerFooter(HTMLProps):
    """The footer of the drawer."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerFooter"


class DrawerTitle(HTMLProps):
    """The title of the drawer."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerTitle"

    # DrawerTitle specific props
    as_child: rx.Var[bool]


class DrawerDescription(HTMLProps):
    """The description of the drawer."""

    library = "$/custom/shadcn/drawer"
    tag = "DrawerDescription"

    # DrawerDescription specific props
    as_child: rx.Var[bool]


class DrawerNamespace(rx.ComponentNamespace):
    root = staticmethod(DrawerRoot.create)
    trigger = staticmethod(DrawerTrigger.create)
    close = staticmethod(DrawerClose.create)
    portal = staticmethod(DrawerPortal.create)
    overlay = staticmethod(DrawerOverlay.create)
    content = staticmethod(DrawerContent.create)
    header = staticmethod(DrawerHeader.create)
    body = staticmethod(DrawerBody.create)
    footer = staticmethod(DrawerFooter.create)
    title = staticmethod(DrawerTitle.create)
    description = staticmethod(DrawerDescription.create)


drawer = DrawerNamespace()


__all__ = [
    "DrawerRoot",
    "DrawerTrigger",
    "DrawerClose",
    "DrawerPortal",
    "DrawerOverlay",
    "DrawerContent",
    "DrawerHeader",
    "DrawerBody",
    "DrawerFooter",
    "DrawerTitle",
    "DrawerDescription",
    "drawer",
    "DrawerNamespace",
]
