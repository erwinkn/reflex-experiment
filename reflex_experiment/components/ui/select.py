from typing import Literal
import reflex as rx
from reflex_experiment.attributes import HTMLProps, HTMLButtonProps
from reflex_experiment.helpers import TypedEventHandler


class SelectRoot(HTMLProps):
    """A select component wrapper based on shadcn/ui."""

    library = "$/custom/shadcn/select"
    tag = "Select"

    # Root specific props
    default_value: rx.Var[str]
    value: rx.Var[str]
    on_value_change: TypedEventHandler[str]
    open: rx.Var[bool]
    default_open: rx.Var[bool]
    on_open_change: TypedEventHandler[bool]
    name: rx.Var[str]
    disabled: rx.Var[bool]


class SelectTrigger(HTMLButtonProps):
    """The trigger for the select component."""

    library = "$/custom/shadcn/select"
    tag = "SelectTrigger"

    # Select trigger specific props
    as_child: rx.Var[bool]


class SelectValue(HTMLProps):
    """The value part of the select component."""

    library = "$/custom/shadcn/select"
    tag = "SelectValue"

    # Select value specific props
    placeholder: rx.Var[str]


class SelectContent(HTMLProps):
    """The content wrapper for the select dropdown."""

    library = "$/custom/shadcn/select"
    tag = "SelectContent"

    # Select content specific props
    position: rx.Var[Literal["item-aligned", "popper"]]
    side: rx.Var[Literal["top", "right", "bottom", "left"]]
    side_offset: rx.Var[int]
    align: rx.Var[Literal["start", "center", "end"]]
    align_offset: rx.Var[int]
    avoid_collisions: rx.Var[bool]


class SelectItem(HTMLProps):
    """An item in the select dropdown."""

    library = "$/custom/shadcn/select"
    tag = "SelectItem"

    # Select item specific props
    value: rx.Var[str]
    disabled: rx.Var[bool]
    text_value: rx.Var[str]


class SelectGroup(HTMLProps):
    """A group of select items."""

    library = "$/custom/shadcn/select"
    tag = "SelectGroup"


class SelectLabel(HTMLProps):
    """A label for a select group."""

    library = "$/custom/shadcn/select"
    tag = "SelectLabel"


class SelectSeparator(HTMLProps):
    """A separator for select items."""

    library = "$/custom/shadcn/select"
    tag = "SelectSeparator"


class SelectNamespace(rx.ComponentNamespace):
    root = staticmethod(SelectRoot.create)
    trigger = staticmethod(SelectTrigger.create)
    value = staticmethod(SelectValue.create)
    content = staticmethod(SelectContent.create)
    item = staticmethod(SelectItem.create)
    group = staticmethod(SelectGroup.create)
    label = staticmethod(SelectLabel.create)
    separator = staticmethod(SelectSeparator.create)


select = SelectNamespace()


__all__ = [
    "SelectRoot",
    "SelectTrigger",
    "SelectValue",
    "SelectContent",
    "SelectItem",
    "SelectGroup",
    "SelectLabel",
    "SelectSeparator",
    "select",
    "SelectNamespace",
]
