import reflex as rx
from reflex_experiment.attributes import HTMLProps


class CardRoot(HTMLProps):
    """A card component based on shadcn/ui."""

    library = "$/custom/shadcn/card"
    tag = "Card"


class CardHeader(HTMLProps):
    """The header of a card component."""

    library = "$/custom/shadcn/card"
    tag = "CardHeader"


class CardTitle(HTMLProps):
    """The title of a card component."""

    library = "$/custom/shadcn/card"
    tag = "CardTitle"


class CardDescription(HTMLProps):
    """The description of a card component."""

    library = "$/custom/shadcn/card"
    tag = "CardDescription"


class CardContent(HTMLProps):
    """The content of a card component."""

    library = "$/custom/shadcn/card"
    tag = "CardContent"


class CardFooter(HTMLProps):
    """The footer of a card component."""

    library = "$/custom/shadcn/card"
    tag = "CardFooter"


class CardNamespace(rx.ComponentNamespace):
    root = staticmethod(CardRoot.create)
    header = staticmethod(CardHeader.create)
    title = staticmethod(CardTitle.create)
    description = staticmethod(CardDescription.create)
    content = staticmethod(CardContent.create)
    footer = staticmethod(CardFooter.create)


card = CardNamespace()


__all__ = [
    "CardRoot",
    "CardHeader",
    "CardTitle",
    "CardDescription",
    "CardContent",
    "CardFooter",
    "card",
    "CardNamespace",
]
