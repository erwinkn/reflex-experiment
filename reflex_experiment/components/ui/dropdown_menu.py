from typing import Literal, TypedDict
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import ButtonHTMLAttributes, HTMLAttributes
from reflex.components.radix.themes.base import RadixThemesComponent


class Foo(TypedDict):
    a: str
    b: int

def test(**kwargs:Foo):
    ...


rx.button

class DropdownMenu(rx.Component):
    """A dropdown menu component based on shadcn/ui."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenu"

    # DropdownMenu specific props
    default_open: rx.Var[bool]
    open: rx.Var[bool]
    on_open_change: rx.EventHandler[lambda open: [open]]
    modal: rx.Var[bool]


class DropdownMenuTrigger(rx.Component, ButtonHTMLAttributes):
    """A trigger for a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuTrigger"

    as_child: rx.Var[bool]


class DropdownMenuGroup(rx.Component, HTMLAttributes):
    """A group of dropdown menu items."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuGroup"

    as_child: rx.Var[bool]


class DropdownMenuPortal(rx.Component):
    """A portal for a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuPortal"

    # DropdownMenuPortal specific props
    force_mount: rx.Var[bool]
    # TODO: support for selecting a container element
    container: rx.Var[str]


class DropdownMenuSub(rx.Component):
    """A submenu within a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuSub"

    # DropdownMenuSub specific props
    default_open: rx.Var[bool]
    open: rx.Var[bool]
    on_open_change: rx.EventHandler[lambda open: [open]]


class DropdownMenuRadioGroup(rx.Component, HTMLAttributes):
    """A radio group within a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuRadioGroup"

    # DropdownMenuRadioGroup specific props
    value: rx.Var[str]
    on_value_change: rx.EventHandler[lambda value: [value]]


class DropdownMenuSubTrigger(rx.Component, HTMLAttributes):
    """A trigger for a dropdown submenu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuSubTrigger"

    # DropdownMenuSubTrigger specific props
    disabled: rx.Var[bool]
    text_value: rx.Var[str]
    as_child: rx.Var[bool]
    inset: rx.Var[bool]


class DropdownMenuSubContent(rx.Component, HTMLAttributes):
    """The content of a dropdown submenu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuSubContent"

    # DropdownMenuSubContent specific props
    as_child: rx.Var[bool]
    loop: rx.Var[bool]
    on_escape_key_down: rx.EventHandler[lambda event: [event]]
    on_pointer_down_outside: rx.EventHandler[lambda event: [event]]
    on_focus_outside: rx.EventHandler[lambda event: [event]]
    on_interact_outside: rx.EventHandler[lambda event: [event]]
    force_mount: rx.Var[bool]
    side_offset: rx.Var[int]
    align_offset: rx.Var[int]
    avoid_collisions: rx.Var[bool]
    collision_boundary: rx.Var[list]
    collision_padding: rx.Var[int | dict]
    arrow_padding: rx.Var[int]
    sticky: rx.Var[Literal["partial", "always"]]
    hide_when_detached: rx.Var[bool]
    # TODO: data attributes


class DropdownMenuContent(rx.Component, HTMLAttributes):
    """The content of a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuContent"

    # DropdownMenuContent specific props
    as_child: rx.Var[bool]
    loop: rx.Var[bool]
    on_close_auto_focus: rx.EventHandler[lambda event: [event]]
    on_escape_key_down: rx.EventHandler[lambda event: [event]]
    on_pointer_down_outside: rx.EventHandler[lambda event: [event]]
    on_focus_outside: rx.EventHandler[lambda event: [event]]
    on_interact_outside: rx.EventHandler[lambda event: [event]]
    force_mount: rx.Var[bool]
    side: rx.Var[Literal["top", "right", "bottom", "left"]]
    side_offset: rx.Var[int]
    align: rx.Var[Literal["start", "center", "end"]]
    align_offset: rx.Var[int]
    avoid_collisions: rx.Var[bool]
    collision_boundary: rx.Var[list]
    collision_padding: rx.Var[int | dict]
    arrow_padding: rx.Var[int]
    sticky: rx.Var[Literal["partial", "always"]]
    hide_when_detached: rx.Var[bool]


class DropdownMenuItem(rx.Component, HTMLAttributes):
    """An item within a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuItem"

    # DropdownMenuItem specific props
    inset: rx.Var[bool]
    disabled: rx.Var[bool]
    text_value: rx.Var[str]
    as_child: rx.Var[bool]
    on_select: rx.EventHandler[lambda event: [event]]


class DropdownMenuCheckboxItem(rx.Component, HTMLAttributes):
    """A checkbox item within a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuCheckboxItem"

    # DropdownMenuCheckboxItem specific props
    checked: rx.Var[bool]
    on_checked_change: rx.EventHandler[lambda checked: [checked]]
    on_select: rx.EventHandler[lambda evt: [evt]]
    disabled: rx.Var[bool]
    text_value: rx.Var[str]
    as_child: rx.Var[bool]
    # TODO: data attributes


class DropdownMenuRadioItem(rx.Component, HTMLAttributes):
    """A radio item within a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuRadioItem"

    # DropdownMenuRadioItem specific props
    value: rx.Var[str]
    disabled: rx.Var[bool]
    text_value: rx.Var[str]
    as_child: rx.Var[bool]
    on_select: rx.EventHandler[lambda evt: [evt]]


class DropdownMenuLabel(rx.Component, HTMLAttributes):
    """A label within a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuLabel"

    # DropdownMenuLabel specific props
    inset: rx.Var[bool]
    as_child: rx.Var[bool]


class DropdownMenuSeparator(rx.Component, HTMLAttributes):
    """A separator within a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuSeparator"

    as_child: rx.Var[bool]


class DropdownMenuShortcut(rx.Component, HTMLAttributes):
    """A keyboard shortcut within a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuShortcut"


# Create helper functions


def dropdown_menu(*children, **props):
    """Create a DropdownMenu component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DropdownMenu.create(*children, **updated_props)


def dropdown_menu_trigger(*children, **props):
    """Create a DropdownMenuTrigger component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DropdownMenuTrigger.create(*children, **updated_props)


def dropdown_menu_group(*children, **props):
    """Create a DropdownMenuGroup component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DropdownMenuGroup.create(*children, **updated_props)


def dropdown_menu_portal(*children, **props):
    """Create a DropdownMenuPortal component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DropdownMenuPortal.create(*children, **updated_props)


def dropdown_menu_sub(*children, **props):
    """Create a DropdownMenuSub component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DropdownMenuSub.create(*children, **updated_props)


def dropdown_menu_radio_group(*children, **props):
    """Create a DropdownMenuRadioGroup component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DropdownMenuRadioGroup.create(*children, **updated_props)


def dropdown_menu_sub_trigger(*children, **props):
    """Create a DropdownMenuSubTrigger component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DropdownMenuSubTrigger.create(*children, **updated_props)


def dropdown_menu_sub_content(*children, **props):
    """Create a DropdownMenuSubContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DropdownMenuSubContent.create(*children, **updated_props)


def dropdown_menu_content(*children, **props):
    """Create a DropdownMenuContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DropdownMenuContent.create(*children, **updated_props)


def dropdown_menu_item(*children, **props):
    """Create a DropdownMenuItem component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DropdownMenuItem.create(*children, **updated_props)


def dropdown_menu_checkbox_item(*children, **props):
    """Create a DropdownMenuCheckboxItem component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DropdownMenuCheckboxItem.create(*children, **updated_props)


def dropdown_menu_radio_item(*children, **props):
    """Create a DropdownMenuRadioItem component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DropdownMenuRadioItem.create(*children, **updated_props)


def dropdown_menu_label(*children, **props):
    """Create a DropdownMenuLabel component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DropdownMenuLabel.create(*children, **updated_props)


def dropdown_menu_separator(*children, **props):
    """Create a DropdownMenuSeparator component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DropdownMenuSeparator.create(*children, **updated_props)


def dropdown_menu_shortcut(*children, **props):
    """Create a DropdownMenuShortcut component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DropdownMenuShortcut.create(*children, **updated_props)


class 


__all__ = [
    "DropdownMenu",
    "dropdown_menu",
    "DropdownMenuTrigger",
    "dropdown_menu_trigger",
    "DropdownMenuGroup",
    "dropdown_menu_group",
    "DropdownMenuPortal",
    "dropdown_menu_portal",
    "DropdownMenuSub",
    "dropdown_menu_sub",
    "DropdownMenuRadioGroup",
    "dropdown_menu_radio_group",
    "DropdownMenuSubTrigger",
    "dropdown_menu_sub_trigger",
    "DropdownMenuSubContent",
    "dropdown_menu_sub_content",
    "DropdownMenuContent",
    "dropdown_menu_content",
    "DropdownMenuItem",
    "dropdown_menu_item",
    "DropdownMenuCheckboxItem",
    "dropdown_menu_checkbox_item",
    "DropdownMenuRadioItem",
    "dropdown_menu_radio_item",
    "DropdownMenuLabel",
    "dropdown_menu_label",
    "DropdownMenuSeparator",
    "dropdown_menu_separator",
    "DropdownMenuShortcut",
    "dropdown_menu_shortcut",
]
