import reflex as rx
from reflex_experiment.attributes import HTMLProps


class Progress(HTMLProps):
    """A progress component based on shadcn/ui."""

    library = "$/custom/shadcn/progress"
    tag = "Progress"

    # Progress specific props
    value: rx.Var[float]
    max: rx.Var[float]
    as_child: rx.Var[bool]
    # TODO: (value: number, max: number) => string
    # get_value_label: rx.Var[str]


progress = Progress.create


__all__ = ["progress", "Progress"]
