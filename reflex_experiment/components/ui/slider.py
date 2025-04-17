from typing import Literal, List, Union
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import GlobalAttributes, HTMLEventHandlersMixin


class Slider(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A slider component based on shadcn/ui."""

    library = "$/custom/shadcn/slider"
    tag = "Slider"

    # Slider specific props
    defaultValue: rx.Var[List[Union[int, float]]] = rx.Var.create([0])
    value: rx.Var[List[Union[int, float]]] = rx.Var.create([0])
    onValueChange: rx.EventHandler[lambda value: [value]]
    onValueCommit: rx.EventHandler[lambda value: [value]]
    min: rx.Var[Union[int, float]] = rx.Var.create(0)
    max: rx.Var[Union[int, float]] = rx.Var.create(100)
    step: rx.Var[Union[int, float]] = rx.Var.create(1)
    orientation: rx.Var[Literal["horizontal", "vertical"]] = rx.Var.create("horizontal")
    disabled: rx.Var[bool] = rx.Var.create(False)
    inverted: rx.Var[bool] = rx.Var.create(False)
    minStepsBetweenThumbs: rx.Var[int] = rx.Var.create(0)


def slider(*children, **props):
    """Create a Slider component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Slider.create(*children, **updated_props)


__all__ = ["Slider", "slider"]
