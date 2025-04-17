from typing import Literal
from reflex_experiment.attributes import HTMLProps
import reflex as rx


class Badge(HTMLProps):
    """A badge component based on shadcn/ui."""

    library = "$/custom/shadcn/badge"
    tag = "Badge"

    # Badge specific props
    variant: rx.Var[Literal["default", "secondary", "destructive", "outline"]]


badge = Badge.create


__all__ = ["badge", "Badge"]
