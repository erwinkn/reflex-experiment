import reflex as rx
from reflex_experiment.attributes import HTMLProps


class PaginationRoot(HTMLProps):
    """A pagination component for navigating through pages."""

    library = "$/custom/shadcn/pagination"
    tag = "Pagination"


class PaginationContent(HTMLProps):
    """The content container for pagination items."""

    library = "$/custom/shadcn/pagination"
    tag = "PaginationContent"


class PaginationItem(HTMLProps):
    """An item within the pagination component."""

    library = "$/custom/shadcn/pagination"
    tag = "PaginationItem"


class PaginationLink(HTMLProps):
    """A link within the pagination component."""

    library = "$/custom/shadcn/pagination"
    tag = "PaginationLink"

    # PaginationLink specific props
    is_active: rx.Var[bool]
    href: rx.Var[str]


class PaginationPrevious(HTMLProps):
    """A button to navigate to the previous page."""

    library = "$/custom/shadcn/pagination"
    tag = "PaginationPrevious"

    # PaginationPrevious specific props
    href: rx.Var[str]


class PaginationNext(HTMLProps):
    """A button to navigate to the next page."""

    library = "$/custom/shadcn/pagination"
    tag = "PaginationNext"

    # PaginationNext specific props
    href: rx.Var[str]


class PaginationEllipsis(HTMLProps):
    """An ellipsis to represent skipped page numbers."""

    library = "$/custom/shadcn/pagination"
    tag = "PaginationEllipsis"


class PaginationNamespace(rx.ComponentNamespace):
    root = staticmethod(PaginationRoot.create)
    content = staticmethod(PaginationContent.create)
    item = staticmethod(PaginationItem.create)
    link = staticmethod(PaginationLink.create)
    previous = staticmethod(PaginationPrevious.create)
    next = staticmethod(PaginationNext.create)
    ellipsis = staticmethod(PaginationEllipsis.create)


pagination = PaginationNamespace()


__all__ = [
    "PaginationRoot",
    "PaginationContent",
    "PaginationItem",
    "PaginationLink",
    "PaginationPrevious",
    "PaginationNext",
    "PaginationEllipsis",
    "pagination",
    "PaginationNamespace",
]
