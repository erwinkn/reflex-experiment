import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import ButtonHTMLAttributes, HTMLAttributes


# Used elsewhere
class DialogAttributes(HTMLAttributes):
    # Dialog specific props
    default_open: rx.Var[bool]
    open: rx.Var[bool]
    on_open_change: rx.EventHandler[lambda open: [open]]
    modal: rx.Var[bool]


class Dialog(rx.Component, DialogAttributes):
    """A dialog component."""

    library = "$/custom/shadcn/dialog"
    tag = "Dialog"


class DialogTrigger(rx.Component, ButtonHTMLAttributes):
    """A button that triggers the dialog."""

    library = "$/custom/shadcn/dialog"
    tag = "DialogTrigger"

    # DialogTrigger specific props
    as_child: rx.Var[bool]


class DialogPortal(rx.Component):
    """A portal for the dialog content."""

    library = "$/custom/shadcn/dialog"
    tag = "DialogPortal"

    # DialogPortal specific props
    force_mount: rx.Var[bool]
    # TODO: convert to HTMLElement
    container: rx.Var[str]


class DialogClose(rx.Component, ButtonHTMLAttributes):
    """A button to close the dialog."""

    library = "$/custom/shadcn/dialog"
    tag = "DialogClose"

    # DialogClose specific props
    as_child: rx.Var[bool]


class DialogContent(rx.Component, HTMLAttributes):
    """The content of the dialog."""

    library = "$/custom/shadcn/dialog"
    tag = "DialogContent"

    # DialogContent specific props
    as_child: rx.Var[bool] = rx.Var.create(False)
    force_mount: rx.Var[bool]
    on_open_auto_focus: rx.EventHandler
    on_close_auto_focus: rx.EventHandler
    on_escape_key_down: rx.EventHandler
    on_pointer_down_outside: rx.EventHandler
    on_interact_outside: rx.EventHandler


class DialogHeader(rx.Component, HTMLAttributes):
    """The header of the dialog."""

    library = "$/custom/shadcn/dialog"
    tag = "DialogHeader"


class DialogFooter(rx.Component, HTMLAttributes):
    """The footer of the dialog."""

    library = "$/custom/shadcn/dialog"
    tag = "DialogFooter"


class DialogTitle(rx.Component, HTMLAttributes):
    """The title of the dialog."""

    library = "$/custom/shadcn/dialog"
    tag = "DialogTitle"

    # DialogTitle specific props
    as_child: rx.Var[bool]


class DialogDescription(rx.Component, HTMLAttributes):
    """The description of the dialog."""

    library = "$/custom/shadcn/dialog"
    tag = "DialogDescription"

    # DialogDescription specific props
    as_child: rx.Var[bool]


# Create helper functions


def dialog(*children, **props):
    """Create a Dialog component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Dialog.create(*children, **updated_props)


def dialog_trigger(*children, **props):
    """Create a DialogTrigger component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DialogTrigger.create(*children, **updated_props)


def dialog_portal(*children, **props):
    """Create a DialogPortal component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DialogPortal.create(*children, **updated_props)


def dialog_close(*children, **props):
    """Create a DialogClose component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DialogClose.create(*children, **updated_props)


def dialog_content(*children, **props):
    """Create a DialogContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DialogContent.create(*children, **updated_props)


def dialog_header(*children, **props):
    """Create a DialogHeader component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DialogHeader.create(*children, **updated_props)


def dialog_footer(*children, **props):
    """Create a DialogFooter component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DialogFooter.create(*children, **updated_props)


def dialog_title(*children, **props):
    """Create a DialogTitle component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DialogTitle.create(*children, **updated_props)


def dialog_description(*children, **props):
    """Create a DialogDescription component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return DialogDescription.create(*children, **updated_props)


__all__ = [
    "Dialog",
    "dialog",
    "DialogTrigger",
    "dialog_trigger",
    "DialogPortal",
    "dialog_portal",
    "DialogClose",
    "dialog_close",
    "DialogContent",
    "dialog_content",
    "DialogHeader",
    "dialog_header",
    "DialogFooter",
    "dialog_footer",
    "DialogTitle",
    "dialog_title",
    "DialogDescription",
    "dialog_description",
]
