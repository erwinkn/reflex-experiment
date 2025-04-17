from typing import Literal, Dict, Any, Callable
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import GlobalAttributes, HTMLEventHandlersMixin, FormElementMixin


class Form(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A form component based on shadcn/ui."""

    library = "$/custom/shadcn/form"
    tag = "Form"

    # Form specific props
    onSubmit: rx.EventHandler[lambda event: [event]]


class FormField(rx.Component, GlobalAttributes):
    """A form field component."""

    library = "$/custom/shadcn/form"
    tag = "FormField"

    # FormField specific props
    name: rx.Var[str] = rx.Var.create("")


class FormItem(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A form item component."""

    library = "$/custom/shadcn/form"
    tag = "FormItem"

    # FormItem specific props
    asChild: rx.Var[bool] = rx.Var.create(False)


class FormLabel(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A form label component."""

    library = "$/custom/shadcn/form"
    tag = "FormLabel"

    # FormLabel specific props
    asChild: rx.Var[bool] = rx.Var.create(False)


class FormControl(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A form control component."""

    library = "$/custom/shadcn/form"
    tag = "FormControl"

    # FormControl specific props
    asChild: rx.Var[bool] = rx.Var.create(False)


class FormDescription(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A form description component."""

    library = "$/custom/shadcn/form"
    tag = "FormDescription"

    # FormDescription specific props
    asChild: rx.Var[bool] = rx.Var.create(False)


class FormMessage(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A form message component."""

    library = "$/custom/shadcn/form"
    tag = "FormMessage"

    # FormMessage specific props
    asChild: rx.Var[bool] = rx.Var.create(False)


# Create helper functions


def form(*children, **props):
    """Create a Form component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Form.create(*children, **updated_props)


def form_field(*children, **props):
    """Create a FormField component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return FormField.create(*children, **updated_props)


def form_item(*children, **props):
    """Create a FormItem component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return FormItem.create(*children, **updated_props)


def form_label(*children, **props):
    """Create a FormLabel component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return FormLabel.create(*children, **updated_props)


def form_control(*children, **props):
    """Create a FormControl component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return FormControl.create(*children, **updated_props)


def form_description(*children, **props):
    """Create a FormDescription component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return FormDescription.create(*children, **updated_props)


def form_message(*children, **props):
    """Create a FormMessage component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return FormMessage.create(*children, **updated_props)


__all__ = [
    "Form",
    "form",
    "FormField",
    "form_field",
    "FormItem",
    "form_item",
    "FormLabel",
    "form_label",
    "FormControl",
    "form_control",
    "FormDescription",
    "form_description",
    "FormMessage",
    "form_message",
]
