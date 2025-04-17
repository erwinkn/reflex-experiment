from typing import Literal, List, Optional, Union, Dict, Any
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import SelectElementMixin, HTMLEventHandlersMixin, GlobalAttributes


class Select(rx.Component, GlobalAttributes):
    """A select component wrapper based on shadcn/ui."""

    library = "$/custom/shadcn/select"
    tag = "Select"


class SelectTrigger(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The trigger for the select component."""

    library = "$/custom/shadcn/select"
    tag = "SelectTrigger"

    # Select trigger specific props
    asChild: rx.Var[bool] = rx.Var.create(False)


class SelectValue(rx.Component, GlobalAttributes):
    """The value part of the select component."""

    library = "$/custom/shadcn/select"
    tag = "SelectValue"

    # Select value specific props
    placeholder: rx.Var[str] = rx.Var.create("")


class SelectContent(rx.Component, GlobalAttributes):
    """The content wrapper for the select dropdown."""

    library = "$/custom/shadcn/select"
    tag = "SelectContent"

    # Select content specific props
    position: rx.Var[Literal["item-aligned", "popper"]] = rx.Var.create("item-aligned")
    side: rx.Var[Literal["top", "right", "bottom", "left"]] = rx.Var.create("bottom")
    sideOffset: rx.Var[int] = rx.Var.create(4)
    align: rx.Var[Literal["start", "center", "end"]] = rx.Var.create("center")
    alignOffset: rx.Var[int] = rx.Var.create(0)
    avoidCollisions: rx.Var[bool] = rx.Var.create(True)


class SelectItem(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """An item in the select dropdown."""

    library = "$/custom/shadcn/select"
    tag = "SelectItem"

    # Select item specific props
    value: rx.Var[str] = rx.Var.create("")
    disabled: rx.Var[bool] = rx.Var.create(False)
    textValue: rx.Var[str] = rx.Var.create("")


class SelectGroup(rx.Component, GlobalAttributes):
    """A group of select items."""

    library = "$/custom/shadcn/select"
    tag = "SelectGroup"


class SelectLabel(rx.Component, GlobalAttributes):
    """A label for a select group."""

    library = "$/custom/shadcn/select"
    tag = "SelectLabel"


class SelectSeparator(rx.Component, GlobalAttributes):
    """A separator for select items."""

    library = "$/custom/shadcn/select"
    tag = "SelectSeparator"


# Create helper functions


def select(*children, **props):
    """Create a Select component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Select.create(*children, **updated_props)


def select_trigger(*children, **props):
    """Create a SelectTrigger component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return SelectTrigger.create(*children, **updated_props)


def select_value(*children, **props):
    """Create a SelectValue component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return SelectValue.create(*children, **updated_props)


def select_content(*children, **props):
    """Create a SelectContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return SelectContent.create(*children, **updated_props)


def select_item(*children, **props):
    """Create a SelectItem component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return SelectItem.create(*children, **updated_props)


def select_group(*children, **props):
    """Create a SelectGroup component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return SelectGroup.create(*children, **updated_props)


def select_label(*children, **props):
    """Create a SelectLabel component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return SelectLabel.create(*children, **updated_props)


def select_separator(*children, **props):
    """Create a SelectSeparator component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return SelectSeparator.create(*children, **updated_props)


__all__ = [
    "Select",
    "select",
    "SelectTrigger",
    "select_trigger",
    "SelectValue",
    "select_value",
    "SelectContent",
    "select_content",
    "SelectItem",
    "select_item",
    "SelectGroup",
    "select_group",
    "SelectLabel",
    "select_label",
    "SelectSeparator",
    "select_separator",
]
