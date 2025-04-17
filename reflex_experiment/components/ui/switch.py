import reflex as rx
from reflex_experiment.attributes import HTMLButtonProps
from reflex_experiment.helpers import TypedEventHandler


class Switch(HTMLButtonProps):
    """A switch component based on shadcn/ui."""

    library = "$/custom/shadcn/switch"
    tag = "Switch"

    # Switch specific props
    checked: rx.Var[bool]
    default_checked: rx.Var[bool]
    on_checked_change: TypedEventHandler[bool]
    as_child: rx.Var[bool]


switch = Switch.create


__all__ = ["switch", "Switch"]
