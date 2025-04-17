import reflex as rx
from reflex_experiment.attributes import HTMLLabelProps


class Label(HTMLLabelProps):
    """A label component based on shadcn/ui."""

    library = "$/custom/shadcn/label"
    tag = "Label"

    # Label specific props
    html_for: rx.Var[str]
    as_child: rx.Var[bool]


label = Label.create


__all__ = ["label", "Label"]
