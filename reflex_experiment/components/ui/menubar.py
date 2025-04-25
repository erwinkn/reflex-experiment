from typing import Literal
import reflex as rx
from reflex_experiment.attributes import HTMLProps, HTMLButtonProps
from reflex_experiment.components.ui.dropdown_menu import Padding
from reflex_experiment.elements import HTMLElement
from reflex_experiment.events import FocusEvent, KeyboardEvent, PointerEvent, SyntheticEvent
from reflex_experiment.helpers import TypedEventHandler


class MenubarRoot(HTMLProps):
    """A menubar component based on shadcn/ui."""

    library = "$/custom/shadcn/menubar"
    tag = "Menubar"

    # Menubar specific props
    default_value: rx.Var[str]
    value: rx.Var[str]
    on_value_change: TypedEventHandler[str]
    loop: rx.Var[bool]


class MenubarMenu(HTMLProps):
    """A menu within a menubar."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarMenu"

    # MenubarMenu specific props
    value: rx.Var[str]
    disabled: rx.Var[bool]


class MenubarTrigger(HTMLButtonProps):
    """A trigger for a menubar menu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarTrigger"

    # MenubarTrigger specific props
    disabled: rx.Var[bool]
    as_child: rx.Var[bool]


class MenubarContent(HTMLProps):
    """The content of a menubar menu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarContent"

    # MenubarContent specific props
    loop: rx.Var[bool]
    force_mount: rx.Var[bool]
    side: rx.Var[Literal["top", "right", "bottom", "left"]]
    side_offset: rx.Var[int]
    align: rx.Var[Literal["start", "center", "end"]]
    align_offset: rx.Var[int]
    avoid_collisions: rx.Var[bool]
    collision_padding: rx.Var[int | Padding]
    on_escape_key_down: TypedEventHandler[KeyboardEvent[HTMLElement]]
    on_pointer_down_outside: TypedEventHandler[PointerEvent[HTMLElement]]
    on_focus_outside: TypedEventHandler[FocusEvent[HTMLElement]]
    # Actually this is PointerEvent | FocusEvent, but not sure the
    # serializer/deserializer can handle this kind of union.
    # If you want the specific event, use on_pointer_down_outside and
    # on_focus_outside.
    on_interact_outside: TypedEventHandler[SyntheticEvent[HTMLElement]]


class MenubarItem(HTMLProps):
    """An item within a menubar menu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarItem"

    # MenubarItem specific props
    inset: rx.Var[bool]
    disabled: rx.Var[bool]
    text_value: rx.Var[str]
    as_child: rx.Var[bool]
    on_select: TypedEventHandler[SyntheticEvent[HTMLElement]]


class MenubarCheckboxItem(HTMLProps):
    """A checkbox item within a menubar menu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarCheckboxItem"

    # MenubarCheckboxItem specific props
    checked: rx.Var[bool]
    on_checked_change: TypedEventHandler[bool]
    disabled: rx.Var[bool]
    text_value: rx.Var[str]
    as_child: rx.Var[bool]


class MenubarRadioGroup(HTMLProps):
    """A radio group within a menubar menu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarRadioGroup"

    # MenubarRadioGroup specific props
    value: rx.Var[str]
    on_value_change: TypedEventHandler[str]


class MenubarRadioItem(HTMLProps):
    """A radio item within a menubar menu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarRadioItem"

    # MenubarRadioItem specific props
    value: rx.Var[str]
    disabled: rx.Var[bool]
    text_value: rx.Var[str]
    as_child: rx.Var[bool]


class MenubarGroup(HTMLProps):
    """A group of menubar items."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarGroup"


class MenubarLabel(HTMLProps):
    """A label within a menubar menu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarLabel"

    # MenubarLabel specific props
    inset: rx.Var[bool]
    as_child: rx.Var[bool]


class MenubarSeparator(HTMLProps):
    """A separator within a menubar menu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarSeparator"


class MenubarShortcut(HTMLProps):
    """A keyboard shortcut displayed in a menubar item."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarShortcut"


class MenubarSub(HTMLProps):
    """A submenu within a menubar menu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarSub"

    # MenubarSub specific props
    default_open: rx.Var[bool]
    open: rx.Var[bool]
    on_open_change: TypedEventHandler[bool]


class MenubarSubTrigger(HTMLButtonProps):
    """A trigger for a menubar submenu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarSubTrigger"

    # MenubarSubTrigger specific props
    inset: rx.Var[bool]
    disabled: rx.Var[bool]
    as_child: rx.Var[bool]


class MenubarSubContent(HTMLProps):
    """The content of a menubar submenu."""

    library = "$/custom/shadcn/menubar"
    tag = "MenubarSubContent"

    # MenubarSubContent specific props
    loop: rx.Var[bool]
    force_mount: rx.Var[bool]
    side: rx.Var[Literal["top", "right", "bottom", "left"]]
    side_offset: rx.Var[int]
    align: rx.Var[Literal["start", "center", "end"]]
    align_offset: rx.Var[int]
    avoid_collisions: rx.Var[bool]
    collision_padding: rx.Var[int | Padding]
    on_escape_key_down: TypedEventHandler[KeyboardEvent[HTMLElement]]
    on_pointer_down_outside: TypedEventHandler[PointerEvent[HTMLElement]]
    on_focus_outside: TypedEventHandler[FocusEvent[HTMLElement]]
    # Actually this is PointerEvent | FocusEvent, but not sure the
    # serializer/deserializer can handle this kind of union.
    # If you want the specific event, use on_pointer_down_outside and
    # on_focus_outside.
    on_interact_outside: TypedEventHandler[SyntheticEvent[HTMLElement]]


class MenubarNamespace(rx.ComponentNamespace):
    root = staticmethod(MenubarRoot.create)
    menu = staticmethod(MenubarMenu.create)
    trigger = staticmethod(MenubarTrigger.create)
    content = staticmethod(MenubarContent.create)
    item = staticmethod(MenubarItem.create)
    checkbox_item = staticmethod(MenubarCheckboxItem.create)
    radio_group = staticmethod(MenubarRadioGroup.create)
    radio_item = staticmethod(MenubarRadioItem.create)
    group = staticmethod(MenubarGroup.create)
    label = staticmethod(MenubarLabel.create)
    separator = staticmethod(MenubarSeparator.create)
    shortcut = staticmethod(MenubarShortcut.create)
    sub = staticmethod(MenubarSub.create)
    sub_trigger = staticmethod(MenubarSubTrigger.create)
    sub_content = staticmethod(MenubarSubContent.create)


menubar = MenubarNamespace()


__all__ = [
    "MenubarRoot",
    "MenubarMenu",
    "MenubarTrigger",
    "MenubarContent",
    "MenubarItem",
    "MenubarCheckboxItem",
    "MenubarRadioGroup",
    "MenubarRadioItem",
    "MenubarGroup",
    "MenubarLabel",
    "MenubarSeparator",
    "MenubarShortcut",
    "MenubarSub",
    "MenubarSubTrigger",
    "MenubarSubContent",
    "menubar",
    "MenubarNamespace",
]
