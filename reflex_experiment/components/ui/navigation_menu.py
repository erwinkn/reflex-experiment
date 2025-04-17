from typing import Literal
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import GlobalAttributes, HTMLEventHandlersMixin, AnchorElementMixin


class NavigationMenu(rx.Component, GlobalAttributes):
    """A navigation menu component based on shadcn/ui."""

    library = "$/custom/shadcn/navigation-menu"
    tag = "NavigationMenu"

    # NavigationMenu specific props
    defaultValue: rx.Var[str] = rx.Var.create("")
    value: rx.Var[str] = rx.Var.create("")
    onValueChange: rx.EventHandler[lambda value: [value]]
    delayDuration: rx.Var[int] = rx.Var.create(200)
    skipDelayDuration: rx.Var[int] = rx.Var.create(300)
    orientation: rx.Var[Literal["horizontal", "vertical"]] = rx.Var.create("horizontal")


class NavigationMenuList(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A list of navigation menu items."""

    library = "$/custom/shadcn/navigation-menu"
    tag = "NavigationMenuList"


class NavigationMenuItem(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """An item within a navigation menu."""

    library = "$/custom/shadcn/navigation-menu"
    tag = "NavigationMenuItem"

    # NavigationMenuItem specific props
    value: rx.Var[str] = rx.Var.create("")
    asChild: rx.Var[bool] = rx.Var.create(False)


class NavigationMenuTrigger(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A trigger for a navigation menu dropdown."""

    library = "$/custom/shadcn/navigation-menu"
    tag = "NavigationMenuTrigger"

    # NavigationMenuTrigger specific props
    asChild: rx.Var[bool] = rx.Var.create(False)


class NavigationMenuContent(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The content for a navigation menu dropdown."""

    library = "$/custom/shadcn/navigation-menu"
    tag = "NavigationMenuContent"

    # NavigationMenuContent specific props
    forceMount: rx.Var[bool] = rx.Var.create(False)
    onEscapeKeyDown: rx.EventHandler[lambda event: [event]]
    onPointerDownOutside: rx.EventHandler[lambda event: [event]]
    onFocusOutside: rx.EventHandler[lambda event: [event]]
    onInteractOutside: rx.EventHandler[lambda event: [event]]


class NavigationMenuLink(rx.Component, AnchorElementMixin, HTMLEventHandlersMixin):
    """A link within a navigation menu."""

    library = "$/custom/shadcn/navigation-menu"
    tag = "NavigationMenuLink"

    # NavigationMenuLink specific props
    active: rx.Var[bool] = rx.Var.create(False)
    onSelect: rx.EventHandler[lambda event: [event]]
    asChild: rx.Var[bool] = rx.Var.create(False)


class NavigationMenuViewport(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The viewport for the navigation menu dropdowns."""

    library = "$/custom/shadcn/navigation-menu"
    tag = "NavigationMenuViewport"

    # NavigationMenuViewport specific props
    forceMount: rx.Var[bool] = rx.Var.create(False)


class NavigationMenuIndicator(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """An indicator for the currently active item."""

    library = "$/custom/shadcn/navigation-menu"
    tag = "NavigationMenuIndicator"

    # NavigationMenuIndicator specific props
    forceMount: rx.Var[bool] = rx.Var.create(False)


# Create helper functions


def navigation_menu(*children, **props):
    """Create a NavigationMenu component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return NavigationMenu.create(*children, **updated_props)


def navigation_menu_list(*children, **props):
    """Create a NavigationMenuList component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return NavigationMenuList.create(*children, **updated_props)


def navigation_menu_item(*children, **props):
    """Create a NavigationMenuItem component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return NavigationMenuItem.create(*children, **updated_props)


def navigation_menu_trigger(*children, **props):
    """Create a NavigationMenuTrigger component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return NavigationMenuTrigger.create(*children, **updated_props)


def navigation_menu_content(*children, **props):
    """Create a NavigationMenuContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return NavigationMenuContent.create(*children, **updated_props)


def navigation_menu_link(*children, **props):
    """Create a NavigationMenuLink component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return NavigationMenuLink.create(*children, **updated_props)


def navigation_menu_viewport(*children, **props):
    """Create a NavigationMenuViewport component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return NavigationMenuViewport.create(*children, **updated_props)


def navigation_menu_indicator(*children, **props):
    """Create a NavigationMenuIndicator component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return NavigationMenuIndicator.create(*children, **updated_props)


__all__ = [
    "NavigationMenu",
    "navigation_menu",
    "NavigationMenuList",
    "navigation_menu_list",
    "NavigationMenuItem",
    "navigation_menu_item",
    "NavigationMenuTrigger",
    "navigation_menu_trigger",
    "NavigationMenuContent",
    "navigation_menu_content",
    "NavigationMenuLink",
    "navigation_menu_link",
    "NavigationMenuViewport",
    "navigation_menu_viewport",
    "NavigationMenuIndicator",
    "navigation_menu_indicator",
]
