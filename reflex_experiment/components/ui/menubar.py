from typing import Literal
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import GlobalAttributes, HTMLEventHandlersMixin


class Menubar(rx.Component, GlobalAttributes):
    """A menubar component based on shadcn/ui."""

    library = "$/custom/shadcn/menubar"
    tag = "Menubar"

    # Menubar specific props
    defaultValue: rx.Var[str] = rx.Var.create("")
    value: rx.Var[str] = rx.Var.create("")
    onValueChange: rx.EventHandler[lambda value: [value]]
    loop: rx.Var[bool] = rx.Var.create(True)


class MenubarMenu(rx.Component, GlobalAttributes):
    """A menu within a menubar."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarMenu"

    # MenubarMenu specific props
    value: rx.Var[str] = rx.Var.create("")
    disabled: rx.Var[bool] = rx.Var.create(False)


class MenubarTrigger(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A trigger for a menubar menu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarTrigger"

    # MenubarTrigger specific props
    disabled: rx.Var[bool] = rx.Var.create(False)
    asChild: rx.Var[bool] = rx.Var.create(False)


class MenubarContent(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The content of a menubar menu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarContent"

    # MenubarContent specific props
    loop: rx.Var[bool] = rx.Var.create(True)
    forceMount: rx.Var[bool] = rx.Var.create(False)
    side: rx.Var[Literal["top", "right", "bottom", "left"]] = rx.Var.create("bottom")
    sideOffset: rx.Var[int] = rx.Var.create(0)
    align: rx.Var[Literal["start", "center", "end"]] = rx.Var[
        Literal["start", "center", "end"]
    ].create("center")
    alignOffset: rx.Var[int] = rx.Var.create(0)
    avoidCollisions: rx.Var[bool] = rx.Var.create(True)
    collisionPadding: rx.Var[int] = rx.Var.create(0)
    onEscapeKeyDown: rx.EventHandler[lambda event: [event]]
    onPointerDownOutside: rx.EventHandler[lambda event: [event]]
    onFocusOutside: rx.EventHandler[lambda event: [event]]
    onInteractOutside: rx.EventHandler[lambda event: [event]]


class MenubarItem(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """An item within a menubar menu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarItem"

    # MenubarItem specific props
    inset: rx.Var[bool] = rx.Var.create(False)
    disabled: rx.Var[bool] = rx.Var.create(False)
    textValue: rx.Var[str] = rx.Var.create("")
    asChild: rx.Var[bool] = rx.Var.create(False)
    onSelect: rx.EventHandler[lambda event: [event]]


class MenubarCheckboxItem(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A checkbox item within a menubar menu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarCheckboxItem"

    # MenubarCheckboxItem specific props
    checked: rx.Var[bool] = rx.Var.create(False)
    onCheckedChange: rx.EventHandler[lambda checked: [checked]]
    disabled: rx.Var[bool] = rx.Var.create(False)
    textValue: rx.Var[str] = rx.Var.create("")
    asChild: rx.Var[bool] = rx.Var.create(False)


class MenubarRadioGroup(rx.Component, GlobalAttributes):
    """A radio group within a menubar menu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarRadioGroup"

    # MenubarRadioGroup specific props
    value: rx.Var[str] = rx.Var.create("")
    onValueChange: rx.EventHandler[lambda value: [value]]


class MenubarRadioItem(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A radio item within a menubar menu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarRadioItem"

    # MenubarRadioItem specific props
    value: rx.Var[str] = rx.Var.create("")
    disabled: rx.Var[bool] = rx.Var.create(False)
    textValue: rx.Var[str] = rx.Var.create("")
    asChild: rx.Var[bool] = rx.Var.create(False)


class MenubarGroup(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A group of menubar items."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarGroup"


class MenubarLabel(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A label within a menubar menu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarLabel"

    # MenubarLabel specific props
    inset: rx.Var[bool] = rx.Var.create(False)
    asChild: rx.Var[bool] = rx.Var.create(False)


class MenubarSeparator(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A separator within a menubar menu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarSeparator"


class MenubarShortcut(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A keyboard shortcut displayed in a menubar item."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarShortcut"


class MenubarSub(rx.Component, GlobalAttributes):
    """A submenu within a menubar menu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarSub"

    # MenubarSub specific props
    defaultOpen: rx.Var[bool] = rx.Var.create(False)
    open: rx.Var[bool] = rx.Var.create(False)
    onOpenChange: rx.EventHandler[lambda open: [open]]


class MenubarSubTrigger(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A trigger for a menubar submenu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarSubTrigger"

    # MenubarSubTrigger specific props
    inset: rx.Var[bool] = rx.Var.create(False)
    disabled: rx.Var[bool] = rx.Var.create(False)
    asChild: rx.Var[bool] = rx.Var.create(False)


class MenubarSubContent(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The content of a menubar submenu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarSubContent"

    # MenubarSubContent specific props
    loop: rx.Var[bool] = rx.Var.create(True)
    forceMount: rx.Var[bool] = rx.Var.create(False)
    side: rx.Var[Literal["top", "right", "bottom", "left"]] = rx.Var.create("right")
    sideOffset: rx.Var[int] = rx.Var.create(-4)
    align: rx.Var[Literal["start", "center", "end"]] = rx.Var.create("center")
    alignOffset: rx.Var[int] = rx.Var.create(0)
    avoidCollisions: rx.Var[bool] = rx.Var.create(True)
    collisionPadding: rx.Var[int] = rx.Var.create(0)
    onEscapeKeyDown: rx.EventHandler[lambda event: [event]]


# Create helper functions


def menubar(*children, **props):
    """Create a Menubar component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Menubar.create(*children, **updated_props)


def menubar_menu(*children, **props):
    """Create a MenubarMenu component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MenubarMenu.create(*children, **updated_props)


def menubar_trigger(*children, **props):
    """Create a MenubarTrigger component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MenubarTrigger.create(*children, **updated_props)


def menubar_content(*children, **props):
    """Create a MenubarContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MenubarContent.create(*children, **updated_props)


def menubar_item(*children, **props):
    """Create a MenubarItem component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MenubarItem.create(*children, **updated_props)


def menubar_checkbox_item(*children, **props):
    """Create a MenubarCheckboxItem component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MenubarCheckboxItem.create(*children, **updated_props)


def menubar_radio_group(*children, **props):
    """Create a MenubarRadioGroup component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MenubarRadioGroup.create(*children, **updated_props)


def menubar_radio_item(*children, **props):
    """Create a MenubarRadioItem component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MenubarRadioItem.create(*children, **updated_props)


def menubar_group(*children, **props):
    """Create a MenubarGroup component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MenubarGroup.create(*children, **updated_props)


def menubar_label(*children, **props):
    """Create a MenubarLabel component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MenubarLabel.create(*children, **updated_props)


def menubar_separator(*children, **props):
    """Create a MenubarSeparator component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MenubarSeparator.create(*children, **updated_props)


def menubar_shortcut(*children, **props):
    """Create a MenubarShortcut component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MenubarShortcut.create(*children, **updated_props)


def menubar_sub(*children, **props):
    """Create a MenubarSub component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MenubarSub.create(*children, **updated_props)


def menubar_sub_trigger(*children, **props):
    """Create a MenubarSubTrigger component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MenubarSubTrigger.create(*children, **updated_props)


def menubar_sub_content(*children, **props):
    """Create a MenubarSubContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MenubarSubContent.create(*children, **updated_props)


__all__ = [
    "Menubar",
    "menubar",
    "MenubarMenu",
    "menubar_menu",
    "MenubarTrigger",
    "menubar_trigger",
    "MenubarContent",
    "menubar_content",
    "MenubarItem",
    "menubar_item",
    "MenubarCheckboxItem",
    "menubar_checkbox_item",
    "MenubarRadioGroup",
    "menubar_radio_group",
    "MenubarRadioItem",
    "menubar_radio_item",
    "MenubarGroup",
    "menubar_group",
    "MenubarLabel",
    "menubar_label",
    "MenubarSeparator",
    "menubar_separator",
    "MenubarShortcut",
    "menubar_shortcut",
    "MenubarSub",
    "menubar_sub",
    "MenubarSubTrigger",
    "menubar_sub_trigger",
    "MenubarSubContent",
    "menubar_sub_content",
]
