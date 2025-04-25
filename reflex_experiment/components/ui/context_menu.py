from typing import Literal
import reflex as rx
from reflex_experiment.attributes import HTMLProps, HTMLButtonProps
from reflex_experiment.components.ui.dropdown_menu import Padding
from reflex_experiment.elements import HTMLElement
from reflex_experiment.events import (
    FocusEvent,
    KeyboardEvent,
    PointerEvent,
    SyntheticEvent,
)
from reflex_experiment.helpers import TypedEventHandler


class ContextMenuRoot(HTMLProps):
    """A context menu component based on shadcn/ui."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenu"

    # ContextMenu specific props
    on_open_change: TypedEventHandler[bool]
    modal: rx.Var[bool]


class ContextMenuTrigger(HTMLButtonProps):
    """A trigger for a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuTrigger"

    # ContextMenuTrigger specific props
    as_child: rx.Var[bool]
    disabled: rx.Var[bool]


class ContextMenuGroup(HTMLProps):
    """A group of context menu items."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuGroup"

    as_child: rx.Var[bool]


class ContextMenuPortal(HTMLProps):
    """A portal for a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuPortal"

    # NOTE: not sure this works with a selection string
    container: rx.Var[str]
    force_mount: rx.Var[bool]


class ContextMenuSub(HTMLProps):
    """A submenu within a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuSub"

    # ContextMenuSub specific props
    open: rx.Var[bool]
    default_open: rx.Var[bool]
    on_open_change: TypedEventHandler[bool]


class ContextMenuRadioGroup(HTMLProps):
    """A radio group within a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuRadioGroup"

    # ContextMenuRadioGroup specific props
    as_child: rx.Var[bool]
    value: rx.Var[str]
    on_value_change: TypedEventHandler[str]


class ContextMenuContent(HTMLProps):
    """The content of a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuContent"

    # ContextMenuContent specific props
    as_child: rx.Var[bool]
    loop: rx.Var[bool]
    force_mount: rx.Var[bool]
    align_offset: rx.Var[int]
    avoid_collisions: rx.Var[bool]
    # Has to be an element or list of elements
    # collision_boundary: rx.Var[List[str]]
    collision_padding: rx.Var[int | Padding]
    sticky: rx.Var[Literal["partial", "always"]]
    hide_when_detached: rx.Var[bool]
    on_close_auto_focus: TypedEventHandler[SyntheticEvent[HTMLElement]]
    on_escape_key_down: TypedEventHandler[KeyboardEvent[HTMLElement]]
    on_pointer_down_outside: TypedEventHandler[PointerEvent[HTMLElement]]
    on_focus_outside: TypedEventHandler[FocusEvent[HTMLElement]]
    # Actually this is PointerEvent | FocusEvent, but not sure the
    # serializer/deserializer can handle this kind of union.
    # If you want the specific event, use on_pointer_down_outside and
    # on_focus_outside.
    on_interact_outside: TypedEventHandler[SyntheticEvent[HTMLElement]]


class ContextMenuItem(HTMLProps):
    """An item in a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuItem"

    # ContextMenuItem specific props
    as_child: rx.Var[bool]
    disabled: rx.Var[bool]
    on_select: TypedEventHandler[SyntheticEvent[HTMLElement]]
    text_value: rx.Var[str]


class ContextMenuRadioItem(HTMLProps):
    """A radio item within a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuRadioItem"

    # ContextMenuRadioItem specific props
    as_child: rx.Var[bool]
    value: rx.Var[str]
    disabled: rx.Var[bool]
    on_select: TypedEventHandler[SyntheticEvent[HTMLElement]]
    text_value: rx.Var[str]


class ContextMenuLabel(HTMLProps):
    """A label within a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuLabel"

    # ContextMenuLabel specific props
    as_child: rx.Var[bool]


class ContextMenuSeparator(HTMLProps):
    """A separator within a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuSeparator"

    as_child: rx.Var[bool]


class ContextMenuShortcut(HTMLProps):
    """A keyboard shortcut within a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuShortcut"


class ContextMenuCheckboxItem(HTMLProps):
    """A checkbox item within a context menu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuCheckboxItem"

    # ContextMenuCheckboxItem specific props
    as_child: rx.Var[bool]
    checked: rx.Var[bool]
    on_checked_change: TypedEventHandler[bool]
    on_select: TypedEventHandler[SyntheticEvent[HTMLElement]]
    disabled: rx.Var[bool]
    text_value: rx.Var[str]


class ContextMenuSubTrigger(HTMLButtonProps):
    """A trigger for a context submenu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuSubTrigger"

    # ContextMenuSubTrigger specific props
    as_child: rx.Var[bool]
    disabled: rx.Var[bool]
    text_value: rx.Var[str]


class ContextMenuSubContent(HTMLProps):
    """The content of a context submenu."""

    library = "$/custom/shadcn/context-menu"
    tag = "ContextMenuSubContent"

    # ContextMenuSubContent specific props
    as_child: rx.Var[bool]
    loop: rx.Var[bool]
    force_mount: rx.Var[bool]
    side_offset: rx.Var[int]
    align_offset: rx.Var[int]
    avoid_collisions: rx.Var[bool]
    # Element or Element[]
    # collision_boundary: rx.Var[List[Any]]
    collision_padding: rx.Var[int | Padding]
    arrow_padding: rx.Var[int]
    sticky: rx.Var[Literal["partial", "always"]]
    hide_when_detached: rx.Var[bool]

    on_escape_key_down: TypedEventHandler[KeyboardEvent[HTMLElement]]
    on_pointer_down_outside: TypedEventHandler[PointerEvent[HTMLElement]]
    on_focus_outside: TypedEventHandler[FocusEvent[HTMLElement]]
    # Actually this is PointerEvent | FocusEvent, but not sure the
    # serializer/deserializer can handle this kind of union.
    # If you want the specific event, use on_pointer_down_outside and
    # on_focus_outside.
    on_interact_outside: TypedEventHandler[SyntheticEvent[HTMLElement]]


class ContextMenuNamespace(rx.ComponentNamespace):
    root = staticmethod(ContextMenuRoot.create)
    trigger = staticmethod(ContextMenuTrigger.create)
    group = staticmethod(ContextMenuGroup.create)
    portal = staticmethod(ContextMenuPortal.create)
    sub = staticmethod(ContextMenuSub.create)
    radio_group = staticmethod(ContextMenuRadioGroup.create)
    content = staticmethod(ContextMenuContent.create)
    item = staticmethod(ContextMenuItem.create)
    radio_item = staticmethod(ContextMenuRadioItem.create)
    label = staticmethod(ContextMenuLabel.create)
    separator = staticmethod(ContextMenuSeparator.create)
    shortcut = staticmethod(ContextMenuShortcut.create)
    checkbox_item = staticmethod(ContextMenuCheckboxItem.create)
    sub_trigger = staticmethod(ContextMenuSubTrigger.create)
    sub_content = staticmethod(ContextMenuSubContent.create)


context_menu = ContextMenuNamespace()


__all__ = [
    "ContextMenuRoot",
    "ContextMenuTrigger",
    "ContextMenuGroup",
    "ContextMenuPortal",
    "ContextMenuSub",
    "ContextMenuRadioGroup",
    "ContextMenuContent",
    "ContextMenuItem",
    "ContextMenuRadioItem",
    "ContextMenuLabel",
    "ContextMenuSeparator",
    "ContextMenuShortcut",
    "ContextMenuCheckboxItem",
    "ContextMenuSubTrigger",
    "ContextMenuSubContent",
    "context_menu",
    "ContextMenuNamespace",
]
