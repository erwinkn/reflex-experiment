from typing import Literal
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import HTMLAttributes


class ContextMenu(rx.Component):
    """A context menu component based on shadcn/ui."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenu"

    # ContextMenu specific props
    # dir included in HTMLAttributes
    on_open_change: rx.EventHandler[lambda open: [open]]
    modal: rx.Var[bool] = rx.Var.create(True)


class ContextMenuTrigger(rx.Component, HTMLAttributes):
    """A trigger for a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuTrigger"

    # ContextMenuTrigger specific props
    as_child: rx.Var[bool]
    disabled: rx.Var[bool]


class ContextMenuGroup(rx.Component, HTMLAttributes):
    """A group of context menu items."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuGroup"

    as_child: rx.Var[bool]


class ContextMenuPortal(rx.Component):
    """A portal for a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuPortal"

    # NOTE: not sure this works with a selection string
    container: rx.Var[str]
    force_mount: rx.Var[bool]


class ContextMenuSub(rx.Component):
    """A submenu within a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuSub"

    # ContextMenuSub specific props
    open: rx.Var[bool]
    default_open: rx.Var[bool]
    on_open_change: rx.EventHandler[lambda open: [open]]


class ContextMenuRadioGroup(rx.Component, HTMLAttributes):
    """A radio group within a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuRadioGroup"

    # ContextMenuRadioGroup specific props
    as_child: rx.Var[bool]
    value: rx.Var[str]
    on_value_change: rx.EventHandler[lambda value: [value]]


class ContextMenuContent(rx.Component, HTMLAttributes):
    """The content of a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuContent"

    # ContextMenuContent specific props
    as_child: rx.Var[bool]
    loop: rx.Var[bool] = rx.Var.create(False)
    on_close_auto_focus: rx.EventHandler[lambda evt: [evt]]
    on_escape_key_down: rx.EventHandler[lambda evt: [evt]]
    on_pointer_down_outside: rx.EventHandler[lambda evt: [evt]]
    on_focus_outside: rx.EventHandler[lambda evt: [evt]]
    on_interact_outside: rx.EventHandler[lambda evt: [evt]]
    force_mount: rx.Var[bool]
    alignOffset: rx.Var[int]
    avoid_collisions: rx.Var[bool]
    # TODO: support elements here
    collision_boundary: rx.Var[list[str]]
    collision_padding: rx.Var[int | float | dict]
    sticky: rx.Var[Literal["partial", "always"]]
    hide_when_detached: rx.Var[bool]


class ContextMenuItem(rx.Component, HTMLAttributes):
    """An item in a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuItem"

    # ContextMenuItem specific props
    as_child: rx.Var[bool]
    disabled: rx.Var[bool]
    on_select: rx.EventHandler[lambda event: [event]]
    text_value: rx.Var[str]


class ContextMenuRadioItem(rx.Component, HTMLAttributes):
    """A radio item within a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuRadioItem"

    # ContextMenuRadioItem specific props
    as_child: rx.Var[bool]
    value: rx.Var[str]
    disabled: rx.Var[bool]
    on_select: rx.EventHandler[lambda event: [event]]
    text_value: rx.Var[str]


class ContextMenuLabel(rx.Component, HTMLAttributes):
    """A label within a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuLabel"

    # ContextMenuLabel specific props
    as_child: rx.Var[bool]


class ContextMenuSeparator(rx.Component, HTMLAttributes):
    """A separator within a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuSeparator"

    as_child: rx.Var[bool]


class ContextMenuShortcut(rx.Component, HTMLAttributes):
    """A keyboard shortcut within a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuShortcut"


class ContextMenuCheckboxItem(rx.Component, HTMLAttributes):
    """A checkbox item within a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuCheckboxItem"

    # ContextMenuCheckboxItem specific props
    as_child: rx.Var[bool]
    checked: rx.Var[bool]
    on_checked_change: rx.EventHandler[lambda checked: [checked]]
    on_select: rx.EventHandler[lambda evt: [evt]]
    disabled: rx.Var[bool]
    text_value: rx.Var[str]


class ContextMenuSubTrigger(rx.Component, HTMLAttributes):
    """A trigger for a context submenu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuSubTrigger"

    # ContextMenuSubTrigger specific props
    as_child: rx.Var[bool]
    disabled: rx.Var[bool]
    text_value: rx.Var[str]


class ContextMenuSubContent(rx.Component, HTMLAttributes):
    """The content of a context submenu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuSubContent"

    # ContextMenuSubContent specific props
    as_child: rx.Var[bool]
    loop: rx.Var[bool]
    on_escape_key_down: rx.EventHandler[lambda evt: [evt]]
    on_pointer_down_outside: rx.EventHandler[lambda evt: [evt]]
    on_focus_outside: rx.EventHandler[lambda evt: [evt]]
    on_interact_outside: rx.EventHandler[lambda evt: [evt]]
    force_mount: rx.Var[bool]
    side_offset: rx.Var[int]
    align_offset: rx.Var[int]
    avoid_collisions: rx.Var[bool]
    collision_boundary: rx.Var[list]
    collision_padding: rx.Var[int | dict]
    arrow_padding: rx.Var[int]
    sticky: rx.Var[Literal["partial", "always"]]
    hide_when_detached: rx.Var[bool]


# Create helper functions


def context_menu(*children, **props):
    """Create a ContextMenu component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ContextMenu.create(*children, **updated_props)


def context_menu_trigger(*children, **props):
    """Create a ContextMenuTrigger component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ContextMenuTrigger.create(*children, **updated_props)


def context_menu_content(*children, **props):
    """Create a ContextMenuContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ContextMenuContent.create(*children, **updated_props)


def context_menu_item(*children, **props):
    """Create a ContextMenuItem component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ContextMenuItem.create(*children, **updated_props)


def context_menu_group(*children, **props):
    """Create a ContextMenuGroup component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ContextMenuGroup.create(*children, **updated_props)


def context_menu_radio_group(*children, **props):
    """Create a ContextMenuRadioGroup component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ContextMenuRadioGroup.create(*children, **updated_props)


def context_menu_radio_item(*children, **props):
    """Create a ContextMenuRadioItem component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ContextMenuRadioItem.create(*children, **updated_props)


def context_menu_label(*children, **props):
    """Create a ContextMenuLabel component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ContextMenuLabel.create(*children, **updated_props)


def context_menu_separator(*children, **props):
    """Create a ContextMenuSeparator component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ContextMenuSeparator.create(*children, **updated_props)


def context_menu_shortcut(*children, **props):
    """Create a ContextMenuShortcut component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ContextMenuShortcut.create(*children, **updated_props)


def context_menu_checkbox_item(*children, **props):
    """Create a ContextMenuCheckboxItem component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ContextMenuCheckboxItem.create(*children, **updated_props)


def context_menu_sub(*children, **props):
    """Create a ContextMenuSub component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ContextMenuSub.create(*children, **updated_props)


def context_menu_sub_trigger(*children, **props):
    """Create a ContextMenuSubTrigger component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ContextMenuSubTrigger.create(*children, **updated_props)


def context_menu_sub_content(*children, **props):
    """Create a ContextMenuSubContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ContextMenuSubContent.create(*children, **updated_props)


def context_menu_portal(*children, **props):
    """Create a ContextMenuPortal component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ContextMenuPortal.create(*children, **updated_props)


__all__ = [
    "ContextMenu",
    "context_menu",
    "ContextMenuTrigger",
    "context_menu_trigger",
    "ContextMenuContent",
    "context_menu_content",
    "ContextMenuItem",
    "context_menu_item",
    "ContextMenuGroup",
    "context_menu_group",
    "ContextMenuRadioGroup",
    "context_menu_radio_group",
    "ContextMenuRadioItem",
    "context_menu_radio_item",
    "ContextMenuLabel",
    "context_menu_label",
    "ContextMenuSeparator",
    "context_menu_separator",
    "ContextMenuShortcut",
    "context_menu_shortcut",
    "ContextMenuCheckboxItem",
    "context_menu_checkbox_item",
    "ContextMenuSub",
    "context_menu_sub",
    "ContextMenuSubTrigger",
    "context_menu_sub_trigger",
    "ContextMenuSubContent",
    "context_menu_sub_content",
    "ContextMenuPortal",
    "context_menu_portal",
]
