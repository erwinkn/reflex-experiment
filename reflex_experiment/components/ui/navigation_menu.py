from typing import Literal
import reflex as rx
from reflex_experiment.attributes import HTMLProps, HTMLButtonProps
from reflex_experiment.elements import HTMLElement
from reflex_experiment.events import (
    FocusEvent,
    KeyboardEvent,
    PointerEvent,
    SyntheticEvent,
)
from reflex_experiment.helpers import TypedEventHandler


class NavigationMenuRoot(HTMLProps):
    """A navigation menu component based on shadcn/ui."""

    library = "$/custom/shadcn/navigation-menu"
    tag = "NavigationMenu"

    # NavigationMenu specific props
    default_value: rx.Var[str]
    value: rx.Var[str]
    on_value_change: TypedEventHandler[str]
    delay_duration: rx.Var[int]
    skip_delay_duration: rx.Var[int]
    orientation: rx.Var[Literal["horizontal", "vertical"]]


class NavigationMenuList(HTMLProps):
    """A list of navigation menu items."""

    library = "$/custom/shadcn/navigation-menu"
    tag = "NavigationMenuList"


class NavigationMenuItem(HTMLProps):
    """An item within a navigation menu."""

    library = "$/custom/shadcn/navigation-menu"
    tag = "NavigationMenuItem"

    # NavigationMenuItem specific props
    value: rx.Var[str]
    as_child: rx.Var[bool]


class NavigationMenuTrigger(HTMLButtonProps):
    """A trigger for a navigation menu dropdown."""

    library = "$/custom/shadcn/navigation-menu"
    tag = "NavigationMenuTrigger"

    # NavigationMenuTrigger specific props
    as_child: rx.Var[bool]


class NavigationMenuContent(HTMLProps):
    """The content for a navigation menu dropdown."""

    library = "$/custom/shadcn/navigation-menu"
    tag = "NavigationMenuContent"

    # NavigationMenuContent specific props
    force_mount: rx.Var[bool]
    on_escape_key_down: TypedEventHandler[KeyboardEvent[HTMLElement]]
    on_pointer_down_outside: TypedEventHandler[PointerEvent[HTMLElement]]
    on_focus_outside: TypedEventHandler[FocusEvent[HTMLElement]]
    # Actually this is PointerEvent | FocusEvent, but not sure the
    # serializer/deserializer can handle this kind of union.
    # If you want the specific event, use on_pointer_down_outside and
    # on_focus_outside.
    on_interact_outside: TypedEventHandler[SyntheticEvent[HTMLElement]]


class NavigationMenuLink(HTMLProps):
    """A link within a navigation menu."""

    library = "$/custom/shadcn/navigation-menu"
    tag = "NavigationMenuLink"

    # NavigationMenuLink specific props
    active: rx.Var[bool]
    as_child: rx.Var[bool]
    on_select: TypedEventHandler[SyntheticEvent[HTMLElement]]


class NavigationMenuViewport(HTMLProps):
    """The viewport for the navigation menu dropdowns."""

    library = "$/custom/shadcn/navigation-menu"
    tag = "NavigationMenuViewport"

    # NavigationMenuViewport specific props
    force_mount: rx.Var[bool]


class NavigationMenuIndicator(HTMLProps):
    """An indicator for the currently active item."""

    library = "$/custom/shadcn/navigation-menu"
    tag = "NavigationMenuIndicator"

    # NavigationMenuIndicator specific props
    force_mount: rx.Var[bool]


class NavigationMenuNamespace(rx.ComponentNamespace):
    root = staticmethod(NavigationMenuRoot.create)
    list = staticmethod(NavigationMenuList.create)
    item = staticmethod(NavigationMenuItem.create)
    trigger = staticmethod(NavigationMenuTrigger.create)
    content = staticmethod(NavigationMenuContent.create)
    link = staticmethod(NavigationMenuLink.create)
    viewport = staticmethod(NavigationMenuViewport.create)
    indicator = staticmethod(NavigationMenuIndicator.create)


navigation_menu = NavigationMenuNamespace()


__all__ = [
    "NavigationMenuRoot",
    "NavigationMenuList",
    "NavigationMenuItem",
    "NavigationMenuTrigger",
    "NavigationMenuContent",
    "NavigationMenuLink",
    "NavigationMenuViewport",
    "NavigationMenuIndicator",
    "navigation_menu",
    "NavigationMenuNamespace",
]
