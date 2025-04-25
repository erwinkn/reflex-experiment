import reflex as rx
from reflex_experiment.attributes import HTMLProps, HTMLButtonProps
from reflex_experiment.helpers import TypedEventHandler
from reflex_experiment.events import (
    KeyboardEvent,
    PointerEvent,
    SyntheticEvent,
    FocusEvent,
)
from reflex_experiment.elements import HTMLElement


class DialogRoot(HTMLProps):
    """A dialog component."""

    library = "$/custom/shadcn/dialog"
    tag = "Dialog"

    # Dialog specific props
    default_open: rx.Var[bool]
    open: rx.Var[bool]
    on_open_change: TypedEventHandler[bool]
    modal: rx.Var[bool]


class DialogTrigger(HTMLButtonProps):
    """A button that triggers the dialog."""

    library = "$/custom/shadcn/dialog"
    tag = "DialogTrigger"

    # DialogTrigger specific props
    as_child: rx.Var[bool]


class DialogPortal(HTMLProps):
    """A portal for the dialog content."""

    library = "$/custom/shadcn/dialog"
    tag = "DialogPortal"

    # DialogPortal specific props
    force_mount: rx.Var[bool]
    # TODO: convert to HTMLElement
    container: rx.Var[str]


class DialogClose(HTMLButtonProps):
    """A button to close the dialog."""

    library = "$/custom/shadcn/dialog"
    tag = "DialogClose"

    # DialogClose specific props
    as_child: rx.Var[bool]


class DialogContent(HTMLProps):
    """The content of the dialog."""

    library = "$/custom/shadcn/dialog"
    tag = "DialogContent"

    # DialogContent specific props
    as_child: rx.Var[bool]
    force_mount: rx.Var[bool]
    on_open_auto_focus: TypedEventHandler[FocusEvent[HTMLElement]]
    on_close_auto_focus: TypedEventHandler[FocusEvent[HTMLElement]]
    on_escape_key_down: TypedEventHandler[KeyboardEvent[HTMLElement]]
    on_pointer_down_outside: TypedEventHandler[PointerEvent[HTMLElement]]
    on_interact_outside: TypedEventHandler[SyntheticEvent[HTMLElement]]


class DialogHeader(HTMLProps):
    """The header of the dialog."""

    library = "$/custom/shadcn/dialog"
    tag = "DialogHeader"


class DialogFooter(HTMLProps):
    """The footer of the dialog."""

    library = "$/custom/shadcn/dialog"
    tag = "DialogFooter"


class DialogTitle(HTMLProps):
    """The title of the dialog."""

    library = "$/custom/shadcn/dialog"
    tag = "DialogTitle"

    # DialogTitle specific props
    as_child: rx.Var[bool]


class DialogDescription(HTMLProps):
    """The description of the dialog."""

    library = "$/custom/shadcn/dialog"
    tag = "DialogDescription"

    # DialogDescription specific props
    as_child: rx.Var[bool]


class DialogNamespace(rx.ComponentNamespace):
    root = staticmethod(DialogRoot.create)
    trigger = staticmethod(DialogTrigger.create)
    portal = staticmethod(DialogPortal.create)
    close = staticmethod(DialogClose.create)
    content = staticmethod(DialogContent.create)
    header = staticmethod(DialogHeader.create)
    footer = staticmethod(DialogFooter.create)
    title = staticmethod(DialogTitle.create)
    description = staticmethod(DialogDescription.create)


dialog = DialogNamespace()


__all__ = [
    "DialogRoot",
    "DialogTrigger",
    "DialogPortal",
    "DialogClose",
    "DialogContent",
    "DialogHeader",
    "DialogFooter",
    "DialogTitle",
    "DialogDescription",
    "dialog",
    "DialogNamespace",
]
