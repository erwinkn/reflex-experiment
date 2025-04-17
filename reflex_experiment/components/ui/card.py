from typing import Literal
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import HTMLAttributes


class Card(rx.Component, HTMLAttributes):
    """A card component based on shadcn/ui."""

    library = "$/custom/shadcn/card"
    tag = "Card"


class CardHeader(rx.Component, HTMLAttributes):
    """The header of a card component."""

    library = "$/custom/shadcn/card"
    tag = "CardHeader"


class CardTitle(rx.Component, HTMLAttributes):
    """The title of a card component."""

    library = "$/custom/shadcn/card"
    tag = "CardTitle"


class CardDescription(rx.Component, HTMLAttributes):
    """The description of a card component."""

    library = "$/custom/shadcn/card"
    tag = "CardDescription"


class CardContent(rx.Component, HTMLAttributes):
    """The content of a card component."""

    library = "$/custom/shadcn/card"
    tag = "CardContent"


class CardFooter(rx.Component, HTMLAttributes):
    """The footer of a card component."""

    library = "$/custom/shadcn/card"
    tag = "CardFooter"


# Create helper functions


def card(*children, **props):
    """Create a Card component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Card.create(*children, **updated_props)


def card_header(*children, **props):
    """Create a CardHeader component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return CardHeader.create(*children, **updated_props)


def card_title(*children, **props):
    """Create a CardTitle component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return CardTitle.create(*children, **updated_props)


def card_description(*children, **props):
    """Create a CardDescription component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return CardDescription.create(*children, **updated_props)


def card_content(*children, **props):
    """Create a CardContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return CardContent.create(*children, **updated_props)


def card_footer(*children, **props):
    """Create a CardFooter component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return CardFooter.create(*children, **updated_props)


__all__ = [
    "Card",
    "card",
    "CardHeader",
    "card_header",
    "CardTitle",
    "card_title",
    "CardDescription",
    "card_description",
    "CardContent",
    "card_content",
    "CardFooter",
    "card_footer",
]
