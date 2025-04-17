from typing import Optional, Dict, Any, Literal
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import GlobalAttributes, HTMLEventHandlersMixin


class Rating(rx.Component, GlobalAttributes):
    """A star rating component."""

    library = "$/custom/shadcn/rating"
    tag = "Rating"

    # Rating specific props
    value: rx.Var[float] = rx.Var.create(0)
    onChange: rx.EventHandler[lambda value: [value]]
    count: rx.Var[int] = rx.Var.create(5)
    max: rx.Var[float] = rx.Var.create(5.0)
    precision: rx.Var[float] = rx.Var.create(1.0)
    readOnly: rx.Var[bool] = rx.Var.create(False)
    disabled: rx.Var[bool] = rx.Var.create(False)
    size: rx.Var[Literal["sm", "md", "lg", "xl"]] = rx.Var.create("md")
    emptyIcon: rx.Var[str] = rx.Var.create("")
    fillIcon: rx.Var[str] = rx.Var.create("")
    halfIcon: rx.Var[str] = rx.Var.create("")
    highlightSelectedOnly: rx.Var[bool] = rx.Var.create(False)
    className: rx.Var[str] = rx.Var.create("")
    style: rx.Var[Dict[str, Any]] = rx.Var.create({})


class RatingItem(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A single item (star) within the rating component."""

    library = "$/custom/shadcn/rating"
    tag = "RatingItem"

    # RatingItem specific props
    index: rx.Var[int] = rx.Var.create(0)
    filled: rx.Var[bool] = rx.Var.create(False)
    halfFilled: rx.Var[bool] = rx.Var.create(False)
    readOnly: rx.Var[bool] = rx.Var.create(False)
    disabled: rx.Var[bool] = rx.Var.create(False)
    size: rx.Var[Literal["sm", "md", "lg", "xl"]] = rx.Var.create("md")
    emptyIcon: rx.Var[str] = rx.Var.create("")
    fillIcon: rx.Var[str] = rx.Var.create("")
    halfIcon: rx.Var[str] = rx.Var.create("")
    className: rx.Var[str] = rx.Var.create("")
    style: rx.Var[Dict[str, Any]] = rx.Var.create({})


class RatingGroup(rx.Component, GlobalAttributes):
    """A group container for rating items."""

    library = "$/custom/shadcn/rating"
    tag = "RatingGroup"

    # RatingGroup specific props
    className: rx.Var[str] = rx.Var.create("")
    style: rx.Var[Dict[str, Any]] = rx.Var.create({})


# Create helper functions


def rating(*children, **props):
    """Create a Rating component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Rating.create(*children, **updated_props)


def rating_item(*children, **props):
    """Create a RatingItem component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return RatingItem.create(*children, **updated_props)


def rating_group(*children, **props):
    """Create a RatingGroup component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return RatingGroup.create(*children, **updated_props)


__all__ = [
    "Rating",
    "rating",
    "RatingItem",
    "rating_item",
    "RatingGroup",
    "rating_group",
]
