from typing import Literal
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import GlobalAttributes, HTMLEventHandlersMixin


class Progress(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A progress component based on shadcn/ui."""

    library = "$/custom/shadcn/progress"
    tag = "Progress"

    # Progress specific props
    value: rx.Var[float] = rx.Var.create(0)
    max: rx.Var[float] = rx.Var.create(100)
    getValueLabel: rx.Var[str] = rx.Var.create("")
    asChild: rx.Var[bool] = rx.Var.create(False)


def progress(*children, **props):
    """Create a Progress component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Progress.create(*children, **updated_props)


__all__ = ["Progress", "progress"]
