# STILL TODO

from typing import Literal, Dict, Any
import reflex as rx
from reflex_experiment.attributes import HTMLProps, HTMLFormProps
from reflex_experiment.helpers import TypedEventHandler


class FormRoot(HTMLFormProps):
    """A form component based on shadcn/ui."""

    library = "$/custom/shadcn/form"
    tag = "Form"

    # Form specific props
    on_submit: TypedEventHandler[Dict[str, Any]]


class FormField(HTMLProps):
    """A form field component."""

    library = "$/custom/shadcn/form"
    tag = "FormField"

    # FormField specific props
    name: rx.Var[str]


class FormItem(HTMLProps):
    """A form item component."""

    library = "$/custom/shadcn/form"
    tag = "FormItem"

    # FormItem specific props
    as_child: rx.Var[bool]


class FormLabel(HTMLProps):
    """A form label component."""

    library = "$/custom/shadcn/form"
    tag = "FormLabel"

    # FormLabel specific props
    as_child: rx.Var[bool]


class FormControl(HTMLProps):
    """A form control component."""

    library = "$/custom/shadcn/form"
    tag = "FormControl"

    # FormControl specific props
    as_child: rx.Var[bool]


class FormDescription(HTMLProps):
    """A form description component."""

    library = "$/custom/shadcn/form"
    tag = "FormDescription"

    # FormDescription specific props
    as_child: rx.Var[bool]


class FormMessage(HTMLProps):
    """A form message component."""

    library = "$/custom/shadcn/form"
    tag = "FormMessage"

    # FormMessage specific props
    as_child: rx.Var[bool]


class FormNamespace(rx.ComponentNamespace):
    root = staticmethod(FormRoot.create)
    field = staticmethod(FormField.create)
    item = staticmethod(FormItem.create)
    label = staticmethod(FormLabel.create)
    control = staticmethod(FormControl.create)
    description = staticmethod(FormDescription.create)
    message = staticmethod(FormMessage.create)


form = FormNamespace()


__all__ = [
    "FormRoot",
    "FormField",
    "FormItem",
    "FormLabel",
    "FormControl",
    "FormDescription",
    "FormMessage",
    "form",
    "FormNamespace",
]
