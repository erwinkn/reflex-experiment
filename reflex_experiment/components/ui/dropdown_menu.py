from typing import Literal, Optional, Union, Dict, List
import reflex as rx
from reflex_experiment.attributes import HTMLProps, HTMLButtonProps
from reflex_experiment.helpers import TypedEventHandler
from reflex_experiment.events import (
    KeyboardEvent,
    PointerEvent,
    FocusEvent,
    SyntheticEvent,
)
from reflex_experiment.elements import HTMLElement


class Padding(rx.Base):
    top: Optional[float]
    bottom: Optional[float]
    left: Optional[float]
    right: Optional[float]


class DropdownMenuRoot(HTMLProps):
    """A dropdown menu component based on shadcn/ui."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenu"

    # DropdownMenu specific props
    default_open: rx.Var[bool]
    open: rx.Var[bool]
    on_open_change: TypedEventHandler[bool]
    modal: rx.Var[bool]


class DropdownMenuTrigger(HTMLButtonProps):
    """A trigger for a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuTrigger"

    as_child: rx.Var[bool]


class DropdownMenuGroup(HTMLProps):
    """A group of dropdown menu items."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuGroup"

    as_child: rx.Var[bool]


class DropdownMenuPortal(HTMLProps):
    """A portal for a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuPortal"

    # DropdownMenuPortal specific props
    force_mount: rx.Var[bool]
    # TODO: support for selecting a container element
    container: rx.Var[str]


class DropdownMenuSub(HTMLProps):
    """A submenu within a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuSub"

    # DropdownMenuSub specific props
    default_open: rx.Var[bool]
    open: rx.Var[bool]
    on_open_change: TypedEventHandler[bool]


class DropdownMenuRadioGroup(HTMLProps):
    """A radio group within a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuRadioGroup"

    # DropdownMenuRadioGroup specific props
    value: rx.Var[str]
    on_value_change: TypedEventHandler[str]


class DropdownMenuSubTrigger(HTMLProps):
    """A trigger for a dropdown submenu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuSubTrigger"

    # DropdownMenuSubTrigger specific props
    disabled: rx.Var[bool]
    text_value: rx.Var[str]
    as_child: rx.Var[bool]
    inset: rx.Var[bool]


class DropdownMenuSubContent(HTMLProps):
    """The content of a dropdown submenu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuSubContent"

    # DropdownMenuSubContent specific props
    as_child: rx.Var[bool]
    loop: rx.Var[bool]
    on_escape_key_down: TypedEventHandler[KeyboardEvent[HTMLElement]]
    on_pointer_down_outside: TypedEventHandler[PointerEvent[HTMLElement]]
    on_focus_outside: TypedEventHandler[FocusEvent[HTMLElement]]
    on_interact_outside: TypedEventHandler[SyntheticEvent[HTMLElement]]
    force_mount: rx.Var[bool]
    side_offset: rx.Var[int]
    align_offset: rx.Var[int]
    avoid_collisions: rx.Var[bool]
    # collision_boundary: rx.Var[List]
    collision_padding: rx.Var[int| Padding]
    arrow_padding: rx.Var[int]
    sticky: rx.Var[Literal["partial", "always"]]
    hide_when_detached: rx.Var[bool]


class DropdownMenuContent(HTMLProps):
    """The content of a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuContent"

    # DropdownMenuContent specific props
    as_child: rx.Var[bool]
    loop: rx.Var[bool]
    on_close_auto_focus: TypedEventHandler[FocusEvent[HTMLElement]]
    on_escape_key_down: TypedEventHandler[KeyboardEvent[HTMLElement]]
    on_pointer_down_outside: TypedEventHandler[PointerEvent[HTMLElement]]
    on_focus_outside: TypedEventHandler[FocusEvent[HTMLElement]]
    on_interact_outside: TypedEventHandler[SyntheticEvent[HTMLElement]]
    force_mount: rx.Var[bool]
    side: rx.Var[Literal["top", "right", "bottom", "left"]]
    side_offset: rx.Var[int]
    align: rx.Var[Literal["start", "center", "end"]]
    align_offset: rx.Var[int]
    avoid_collisions: rx.Var[bool]
    collision_boundary: rx.Var[List]
    collision_padding: rx.Var[int| Padding]
    arrow_padding: rx.Var[int]
    sticky: rx.Var[Literal["partial", "always"]]
    hide_when_detached: rx.Var[bool]


class DropdownMenuItem(HTMLProps):
    """An item within a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuItem"

    # DropdownMenuItem specific props
    inset: rx.Var[bool]
    disabled: rx.Var[bool]
    text_value: rx.Var[str]
    as_child: rx.Var[bool]
    on_select: TypedEventHandler[SyntheticEvent[HTMLElement]]


class DropdownMenuCheckboxItem(HTMLProps):
    """A checkbox item within a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuCheckboxItem"

    # DropdownMenuCheckboxItem specific props
    checked: rx.Var[bool]
    on_checked_change: TypedEventHandler[bool]
    on_select: TypedEventHandler[SyntheticEvent[HTMLElement]]
    disabled: rx.Var[bool]
    text_value: rx.Var[str]
    as_child: rx.Var[bool]


class DropdownMenuRadioItem(HTMLProps):
    """A radio item within a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuRadioItem"

    # DropdownMenuRadioItem specific props
    value: rx.Var[str]
    disabled: rx.Var[bool]
    text_value: rx.Var[str]
    as_child: rx.Var[bool]
    on_select: TypedEventHandler[SyntheticEvent[HTMLElement]]


class DropdownMenuLabel(HTMLProps):
    """A label within a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuLabel"

    # DropdownMenuLabel specific props
    inset: rx.Var[bool]
    as_child: rx.Var[bool]


class DropdownMenuSeparator(HTMLProps):
    """A separator within a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuSeparator"

    as_child: rx.Var[bool]


class DropdownMenuShortcut(HTMLProps):
    """A keyboard shortcut within a dropdown menu."""

    library = "$/custom/shadcn/dropdown-menu"
    tag = "DropdownMenuShortcut"


class DropdownMenuNamespace(rx.ComponentNamespace):
    root = staticmethod(DropdownMenuRoot.create)
    trigger = staticmethod(DropdownMenuTrigger.create)
    group = staticmethod(DropdownMenuGroup.create)
    portal = staticmethod(DropdownMenuPortal.create)
    sub = staticmethod(DropdownMenuSub.create)
    radio_group = staticmethod(DropdownMenuRadioGroup.create)
    sub_trigger = staticmethod(DropdownMenuSubTrigger.create)
    sub_content = staticmethod(DropdownMenuSubContent.create)
    content = staticmethod(DropdownMenuContent.create)
    item = staticmethod(DropdownMenuItem.create)
    checkbox_item = staticmethod(DropdownMenuCheckboxItem.create)
    radio_item = staticmethod(DropdownMenuRadioItem.create)
    label = staticmethod(DropdownMenuLabel.create)
    separator = staticmethod(DropdownMenuSeparator.create)
    shortcut = staticmethod(DropdownMenuShortcut.create)


dropdown_menu = DropdownMenuNamespace()


__all__ = [
    "DropdownMenuRoot",
    "DropdownMenuTrigger",
    "DropdownMenuGroup",
    "DropdownMenuPortal",
    "DropdownMenuSub",
    "DropdownMenuRadioGroup",
    "DropdownMenuSubTrigger",
    "DropdownMenuSubContent",
    "DropdownMenuContent",
    "DropdownMenuItem",
    "DropdownMenuCheckboxItem",
    "DropdownMenuRadioItem",
    "DropdownMenuLabel",
    "DropdownMenuSeparator",
    "DropdownMenuShortcut",
    "dropdown_menu",
    "DropdownMenuNamespace",
]
