from typing import Any, Literal
import reflex as rx
from reflex_experiment.attributes import HTMLProps, HTMLButtonProps


class CarouselRoot(HTMLProps):
    """A carousel component based on shadcn/ui."""

    library = "$/custom/shadcn/carousel"
    tag = "Carousel"
    lib_dependencies = ["embla-carousel-react"]

    # Carousel specific props
    orientation: rx.Var[Literal["horizontal", "vertical"]]

    opts: rx.Var[dict[str, Any]]
    # Can't handle those ones in Python
    # plugins: rx.Var[list[Any]]
    # set_api: TypedEventHandler[Any]


class CarouselContent(HTMLProps):
    """The content container of a carousel."""

    library = "$/custom/shadcn/carousel"
    tag = "CarouselContent"


class CarouselItem(HTMLProps):
    """An item within a carousel."""

    library = "$/custom/shadcn/carousel"
    tag = "CarouselItem"


class CarouselPrevious(HTMLButtonProps):
    """A button to navigate to the previous item."""

    library = "$/custom/shadcn/carousel"
    tag = "CarouselPrevious"


class CarouselNext(HTMLButtonProps):
    """A button to navigate to the next item."""

    library = "$/custom/shadcn/carousel"
    tag = "CarouselNext"


class CarouselNamespace(rx.ComponentNamespace):
    root = staticmethod(CarouselRoot.create)
    content = staticmethod(CarouselContent.create)
    item = staticmethod(CarouselItem.create)
    previous = staticmethod(CarouselPrevious.create)
    next = staticmethod(CarouselNext.create)


carousel = CarouselNamespace()


__all__ = [
    "CarouselRoot",
    "CarouselContent",
    "CarouselItem",
    "CarouselPrevious",
    "CarouselNext",
    "carousel",
    "CarouselNamespace",
]
