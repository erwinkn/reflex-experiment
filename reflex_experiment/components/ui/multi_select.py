from typing import List, Dict, Any, Optional, Union, Literal
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import GlobalAttributes, HTMLEventHandlersMixin


class MultiSelect(rx.Component, GlobalAttributes):
    """A multi-select component for selecting multiple items from a dropdown list."""

    library = "$/custom/shadcn/multi-select"
    tag = "MultiSelect"

    # MultiSelect specific props
    defaultValue: rx.Var[List[str]] = rx.Var.create([])
    value: rx.Var[List[str]] = rx.Var.create([])
    onValueChange: rx.EventHandler[lambda value: [value]]
    placeholder: rx.Var[str] = rx.Var.create("Select items...")
    disabled: rx.Var[bool] = rx.Var.create(False)
    items: rx.Var[List[Dict[str, Any]]] = rx.Var.create([])
    className: rx.Var[str] = rx.Var.create("")
    badges: rx.Var[bool] = rx.Var.create(True)
    popoverAlign: rx.Var[Literal["start", "center", "end"]] = rx.Var.create("start")
    clearable: rx.Var[bool] = rx.Var.create(True)
    searchable: rx.Var[bool] = rx.Var.create(True)
    emptyIndicator: rx.Var[str] = rx.Var.create("No results found.")


class MultiSelectTrigger(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The trigger button for a multi-select dropdown."""

    library = "$/custom/shadcn/multi-select"
    tag = "MultiSelectTrigger"

    # MultiSelectTrigger specific props
    className: rx.Var[str] = rx.Var.create("")


class MultiSelectValue(rx.Component, GlobalAttributes):
    """The value display area for a multi-select component."""

    library = "$/custom/shadcn/multi-select"
    tag = "MultiSelectValue"

    # MultiSelectValue specific props
    placeholder: rx.Var[str] = rx.Var.create("Select items...")


class MultiSelectContent(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The content container for a multi-select dropdown."""

    library = "$/custom/shadcn/multi-select"
    tag = "MultiSelectContent"

    # MultiSelectContent specific props
    align: rx.Var[Literal["start", "center", "end"]] = rx.Var.create("start")
    sideOffset: rx.Var[int] = rx.Var.create(4)
    className: rx.Var[str] = rx.Var.create("")


class MultiSelectItem(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """An item within a multi-select dropdown."""

    library = "$/custom/shadcn/multi-select"
    tag = "MultiSelectItem"

    # MultiSelectItem specific props
    value: rx.Var[str] = rx.Var.create("")
    textValue: rx.Var[str] = rx.Var.create("")
    disabled: rx.Var[bool] = rx.Var.create(False)
    className: rx.Var[str] = rx.Var.create("")


class MultiSelectBadge(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A badge representing a selected item in the multi-select component."""

    library = "$/custom/shadcn/multi-select"
    tag = "MultiSelectBadge"

    # MultiSelectBadge specific props
    value: rx.Var[str] = rx.Var.create("")
    onRemove: rx.EventHandler[lambda value: [value]]
    className: rx.Var[str] = rx.Var.create("")


class MultiSelectSeparator(rx.Component, GlobalAttributes):
    """A separator between multi-select items or groups."""

    library = "$/custom/shadcn/multi-select"
    tag = "MultiSelectSeparator"

    # MultiSelectSeparator specific props
    className: rx.Var[str] = rx.Var.create("")


# Create helper functions


def multi_select(*children, **props):
    """Create a MultiSelect component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MultiSelect.create(*children, **updated_props)


def multi_select_trigger(*children, **props):
    """Create a MultiSelectTrigger component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MultiSelectTrigger.create(*children, **updated_props)


def multi_select_value(*children, **props):
    """Create a MultiSelectValue component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MultiSelectValue.create(*children, **updated_props)


def multi_select_content(*children, **props):
    """Create a MultiSelectContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MultiSelectContent.create(*children, **updated_props)


def multi_select_item(*children, **props):
    """Create a MultiSelectItem component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MultiSelectItem.create(*children, **updated_props)


def multi_select_badge(*children, **props):
    """Create a MultiSelectBadge component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MultiSelectBadge.create(*children, **updated_props)


def multi_select_separator(*children, **props):
    """Create a MultiSelectSeparator component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return MultiSelectSeparator.create(*children, **updated_props)


__all__ = [
    "MultiSelect",
    "multi_select",
    "MultiSelectTrigger",
    "multi_select_trigger",
    "MultiSelectValue",
    "multi_select_value",
    "MultiSelectContent",
    "multi_select_content",
    "MultiSelectItem",
    "multi_select_item",
    "MultiSelectBadge",
    "multi_select_badge",
    "MultiSelectSeparator",
    "multi_select_separator",
]
