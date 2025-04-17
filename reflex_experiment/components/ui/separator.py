from typing import Literal
import reflex as rx
from reflex_experiment.attributes import HTMLProps


class Separator(HTMLProps):
    """A separator component based on shadcn/ui."""

    library = "$/custom/shadcn/separator"
    tag = "Separator"

    # Separator specific props
    orientation: rx.Var[Literal["horizontal", "vertical"]]
    decorative: rx.Var[bool]
    as_child: rx.Var[bool]


separator = Separator.create


__all__ = ["separator", "Separator"]
