from typing import Literal
import reflex as rx
from reflex_experiment.attributes import HTMLButtonProps
from reflex_experiment.helpers import TypedEventHandler


class Checkbox(HTMLButtonProps):
    """A checkbox component based on shadcn/ui."""

    library = "$/custom/shadcn/checkbox"
    tag = "Checkbox"

    # Checkbox specific props
    as_child: rx.Var[bool]
    default_checked: rx.Var[bool]
    checked: rx.Var[bool]
    on_checked_change: TypedEventHandler[bool | Literal["indeterminate"]]
    required: rx.Var[bool]


checkbox = Checkbox.create


__all__ = ["checkbox", "Checkbox"]
