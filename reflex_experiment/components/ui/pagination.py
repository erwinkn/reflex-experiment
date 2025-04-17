from typing import Optional, Dict, Any
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import GlobalAttributes, HTMLEventHandlersMixin


class Pagination(rx.Component, GlobalAttributes):
    """A pagination component for navigating through pages."""

    library = "$/custom/shadcn/pagination"
    tag = "Pagination"


class PaginationContent(rx.Component, GlobalAttributes):
    """The content container for pagination items."""

    library = "$/custom/shadcn/pagination"
    tag = "PaginationContent"


class PaginationItem(rx.Component, GlobalAttributes):
    """An item within the pagination component."""

    library = "$/custom/shadcn/pagination"
    tag = "PaginationItem"


class PaginationLink(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A link within the pagination component."""

    library = "$/custom/shadcn/pagination"
    tag = "PaginationLink"

    # PaginationLink specific props
    isActive: rx.Var[bool] = rx.Var.create(False)
    href: rx.Var[str] = rx.Var.create("#")


class PaginationPrevious(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A button to navigate to the previous page."""

    library = "$/custom/shadcn/pagination"
    tag = "PaginationPrevious"

    # PaginationPrevious specific props
    href: rx.Var[str] = rx.Var.create("#")


class PaginationNext(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A button to navigate to the next page."""

    library = "$/custom/shadcn/pagination"
    tag = "PaginationNext"

    # PaginationNext specific props
    href: rx.Var[str] = rx.Var.create("#")


class PaginationEllipsis(rx.Component, GlobalAttributes):
    """An ellipsis to represent skipped page numbers."""

    library = "$/custom/shadcn/pagination"
    tag = "PaginationEllipsis"


# Create helper functions


def pagination(*children, **props):
    """Create a Pagination component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Pagination.create(*children, **updated_props)


def pagination_content(*children, **props):
    """Create a PaginationContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return PaginationContent.create(*children, **updated_props)


def pagination_item(*children, **props):
    """Create a PaginationItem component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return PaginationItem.create(*children, **updated_props)


def pagination_link(*children, **props):
    """Create a PaginationLink component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return PaginationLink.create(*children, **updated_props)


def pagination_previous(*children, **props):
    """Create a PaginationPrevious component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return PaginationPrevious.create(*children, **updated_props)


def pagination_next(*children, **props):
    """Create a PaginationNext component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return PaginationNext.create(*children, **updated_props)


def pagination_ellipsis(*children, **props):
    """Create a PaginationEllipsis component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return PaginationEllipsis.create(*children, **updated_props)


__all__ = [
    "Pagination",
    "pagination",
    "PaginationContent",
    "pagination_content",
    "PaginationItem",
    "pagination_item",
    "PaginationLink",
    "pagination_link",
    "PaginationPrevious",
    "pagination_previous",
    "PaginationNext",
    "pagination_next",
    "PaginationEllipsis",
    "pagination_ellipsis",
]
