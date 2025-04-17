import reflex as rx
from reflex_experiment.attributes import (
    HTMLProps,
    HTMLAnchorProps,
    HTMLOlProps,
    HTMLLiProps,
)


class BreadcrumbRoot(HTMLProps):
    """A breadcrumb component based on shadcn/ui."""

    library = "$/custom/shadcn/breadcrumb"
    tag = "Breadcrumb"


class BreadcrumbList(HTMLOlProps):
    """The container for breadcrumb items."""

    library = "$/custom/shadcn/breadcrumb"
    tag = "BreadcrumbList"


class BreadcrumbItem(HTMLLiProps):
    """An item in a breadcrumb trail."""

    library = "$/custom/shadcn/breadcrumb"
    tag = "BreadcrumbItem"


class BreadcrumbLink(HTMLAnchorProps):
    """A link within a breadcrumb item."""

    library = "$/custom/shadcn/breadcrumb"
    tag = "BreadcrumbLink"

    # BreadcrumbLink specific props
    as_child: rx.Var[bool]


class BreadcrumbPage(HTMLProps):
    """The current page marker in a breadcrumb trail."""

    library = "$/custom/shadcn/breadcrumb"
    tag = "BreadcrumbPage"


class BreadcrumbSeparator(HTMLLiProps):
    """A separator between breadcrumb items."""

    library = "$/custom/shadcn/breadcrumb"
    tag = "BreadcrumbSeparator"


class BreadcrumbEllipsis(HTMLProps):
    """An ellipsis for collapsed breadcrumb items."""

    library = "$/custom/shadcn/breadcrumb"
    tag = "BreadcrumbEllipsis"


class BreadcrumbNamespace(rx.ComponentNamespace):
    root = staticmethod(BreadcrumbRoot.create)
    list = staticmethod(BreadcrumbList.create)
    item = staticmethod(BreadcrumbItem.create)
    link = staticmethod(BreadcrumbLink.create)
    page = staticmethod(BreadcrumbPage.create)
    separator = staticmethod(BreadcrumbSeparator.create)
    ellipsis = staticmethod(BreadcrumbEllipsis.create)


breadcrumb = BreadcrumbNamespace()


__all__ = [
    "BreadcrumbRoot",
    "BreadcrumbList",
    "BreadcrumbItem",
    "BreadcrumbLink",
    "BreadcrumbPage",
    "BreadcrumbSeparator",
    "BreadcrumbEllipsis",
    "breadcrumb",
    "BreadcrumbNamespace",
]
