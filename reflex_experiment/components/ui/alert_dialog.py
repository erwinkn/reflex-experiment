import reflex as rx

from reflex_experiment.attributes import HTMLButtonProps, HTMLProps


class AlertDialog(HTMLProps):
    """An alert dialog component."""

    library = "$/custom/shadcn/alert-dialog"
    tag = "AlertDialog"

    # AlertDialog specific props
    default_open: rx.Var[bool]
    open: rx.Var[bool]
    on_open_change: rx.EventHandler[lambda open: [open]]


class AlertDialogTrigger(HTMLProps):
    """A button that triggers the alert dialog."""

    library = "$/custom/shadcn/alert-dialog"
    tag = "AlertDialogTrigger"

    # AlertDialogTrigger specific props
    as_child: rx.Var[bool]


class AlertDialogPortal(HTMLProps):
    """A portal for the alert dialog content."""

    library = "$/custom/shadcn/alert-dialog"
    tag = "AlertDialogPortal"

    # AlertDialogPortal specific props
    force_mount: rx.Var[bool]
    container: rx.Var[
        str
    ]  # Note: supposed to be an HTMLDivElement, not sure selector strings work


class AlertDialogOverlay(HTMLProps):
    """The overlay for the alert dialog."""

    library = "$/custom/shadcn/alert-dialog"
    tag = "AlertDialogOverlay"

    # AlertDialogOverlay specific props
    as_child: rx.Var[bool]
    force_mount: rx.Var[bool]


class AlertDialogContent( HTMLProps):
    """The content of the alert dialog."""

    library = "$/custom/shadcn/alert-dialog"
    tag = "AlertDialogContent"

    # AlertDialogContent specific props
    as_child: rx.Var[bool]
    force_mount: rx.Var[bool]
    on_open_auto_focus: rx.EventHandler[lambda event: [event]]
    on_close_auto_focus: rx.EventHandler[lambda event: [event]]
    on_escape_key_down: rx.EventHandler[lambda event: [event]]


class AlertDialogHeader(HTMLProps):
    """The header of the alert dialog."""

    library = "$/custom/shadcn/alert-dialog"
    tag = "AlertDialogHeader"


class AlertDialogFooter(HTMLProps):
    """The footer of the alert dialog."""

    library = "$/custom/shadcn/alert-dialog"
    tag = "AlertDialogFooter"


class AlertDialogTitle(HTMLProps):
    """The title of the alert dialog."""

    library = "$/custom/shadcn/alert-dialog"
    tag = "AlertDialogTitle"

    # AlertDialogTitle specific props
    as_child: rx.Var[bool]


class AlertDialogDescription(HTMLProps):
    """The description of the alert dialog."""

    library = "$/custom/shadcn/alert-dialog"
    tag = "AlertDialogDescription"

    # AlertDialogDescription specific props
    as_child: rx.Var[bool]


class AlertDialogAction(HTMLButtonProps):
    """An action button in the alert dialog."""

    library = "$/custom/shadcn/alert-dialog"
    tag = "AlertDialogAction"

    # AlertDialogAction specific props
    as_child: rx.Var[bool]


class AlertDialogCancel(HTMLButtonProps):
    """A cancel button in the alert dialog."""

    library = "$/custom/shadcn/alert-dialog"
    tag = "AlertDialogCancel"

    # AlertDialogCancel specific props
    as_child: rx.Var[bool]



class AlertDialogNamespace(rx.ComponentNamespace):
    root = staticmethod(AlertDialog.create)
    trigger = staticmethod(AlertDialogTrigger.create)
    portal = staticmethod(AlertDialogPortal.create)
    overlay = staticmethod(AlertDialogOverlay.create)
    content = staticmethod(AlertDialogContent.create)
    header = staticmethod(AlertDialogHeader.create)
    footer = staticmethod(AlertDialogFooter.create)
    title = staticmethod(AlertDialogTitle.create)
    description = staticmethod(AlertDialogDescription.create)
    action = staticmethod(AlertDialogAction.create)
    cancel = staticmethod(AlertDialogCancel.create)


alert_dialog = AlertDialogNamespace()


__all__ = [
    "AlertDialog",
    "AlertDialogTrigger", 
    "AlertDialogPortal",
    "AlertDialogOverlay",
    "AlertDialogContent",
    "AlertDialogHeader",
    "AlertDialogFooter", 
    "AlertDialogTitle",
    "AlertDialogDescription",
    "AlertDialogAction",
    "AlertDialogCancel",
    "alert_dialog",
]
