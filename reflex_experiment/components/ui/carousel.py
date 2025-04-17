from typing import Literal, Any
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from stoneware_app.components.ui.button import ButtonAttributes
from ..attributes import HTMLAttributes


class Carousel(rx.Component, HTMLAttributes):
    """A carousel component based on shadcn/ui."""

    library = "$/custom/shadcn/carousel"
    tag = "Carousel"
    lib_dependencies = ["embla-carousel-react"]

    # Carousel specific props
    orientation: rx.Var[Literal["horizontal", "vertical"]]
    opts: rx.Var[dict[str, Any]]
    plugins: rx.Var[list[Any]]
    setApi: rx.EventHandler[lambda api: [api]]


class CarouselContent(rx.Component, HTMLAttributes):
    """The content container of a carousel."""

    library = "$/custom/shadcn/carousel"
    tag = "CarouselContent"


class CarouselItem(rx.Component, HTMLAttributes):
    """An item within a carousel."""

    library = "$/custom/shadcn/carousel"
    tag = "CarouselItem"


# Wraps a shadcn Button
class CarouselPrevious(rx.Component, ButtonAttributes):
    """A button to navigate to the previous item."""

    library = "$/custom/shadcn/carousel"
    tag = "CarouselPrevious"


# Wraps a shadcn Button
class CarouselNext(rx.Component, ButtonAttributes):
    """A button to navigate to the next item."""

    library = "$/custom/shadcn/carousel"
    tag = "CarouselNext"


# Create helper functions


def carousel(*children, **props):
    """Create a Carousel component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Carousel.create(*children, **updated_props)


def carousel_content(*children, **props):
    """Create a CarouselContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return CarouselContent.create(*children, **updated_props)


def carousel_item(*children, **props):
    """Create a CarouselItem component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return CarouselItem.create(*children, **updated_props)


def carousel_previous(*children, **props):
    """Create a CarouselPrevious component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return CarouselPrevious.create(*children, **updated_props)


def carousel_next(*children, **props):
    """Create a CarouselNext component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return CarouselNext.create(*children, **updated_props)


__all__ = [
    "Carousel",
    "carousel",
    "CarouselContent",
    "carousel_content",
    "CarouselItem",
    "carousel_item",
    "CarouselPrevious",
    "carousel_previous",
    "CarouselNext",
    "carousel_next",
]
