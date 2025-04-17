from typing import Literal
import reflex as rx

from reflex_experiment.attributes import HTMLProps


class AlertRoot(HTMLProps):
    """An alert component based on shadcn/ui."""

    library = "$/custom/shadcn/alert"
    tag = "Alert"

    # Alert specific props
    variant: rx.Var[Literal["default", "destructive"]] = "default"  # type: ignore


class AlertTitle(HTMLProps):
    """The title of an alert component."""

    library = "$/custom/shadcn/alert"
    tag = "AlertTitle"


class AlertDescription(HTMLProps):
    """The description of an alert component."""

    library = "$/custom/shadcn/alert"
    tag = "AlertDescription"


class AlertNamespace(rx.ComponentNamespace):
    root = staticmethod(AlertRoot.create)
    title = staticmethod(AlertTitle.create)
    description = staticmethod(AlertDescription.create)


alert = AlertNamespace()


__all__ = ["alert", "AlertRoot", "AlertTitle", "AlertDescription", "AlertNamespace"]
