from typing import Literal
import reflex as rx
from reflex_experiment.attributes import HTMLProps
from reflex_experiment.helpers import TypedEventHandler


class Slider(HTMLProps):
    """A slider component based on shadcn/ui."""

    library = "$/custom/shadcn/slider"
    tag = "Slider"

    # Slider specific props
    default_value: rx.Var[list[float]]
    value: rx.Var[list[float]]
    on_value_change: TypedEventHandler[list[float]]
    on_value_commit: TypedEventHandler[list[float]]
    min: rx.Var[float]
    max: rx.Var[float]
    step: rx.Var[float]
    orientation: rx.Var[Literal["horizontal", "vertical"]]
    disabled: rx.Var[bool]
    inverted: rx.Var[bool]
    min_steps_between_thumbs: rx.Var[int]
    # skipped: form


slider = Slider.create


__all__ = ["slider", "Slider"]
