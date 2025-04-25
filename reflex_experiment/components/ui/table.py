import reflex as rx
from reflex_experiment.attributes import (
    HTMLProps,
    HTMLTableProps,
    HTMLTdProps,
    HTMLThProps,
)


class TableRoot(HTMLTableProps):
    """A table component based on shadcn/ui."""

    library = "$/custom/shadcn/table"
    tag = "Table"


class TableHeader(HTMLProps):
    """The header of a table."""

    library = "$/custom/shadcn/table"
    tag = "TableHeader"


class TableBody(HTMLProps):
    """The body of a table."""

    library = "$/custom/shadcn/table"
    tag = "TableBody"


class TableFooter(HTMLProps):
    """The footer of a table."""

    library = "$/custom/shadcn/table"
    tag = "TableFooter"


class TableRow(HTMLProps):
    """A row in a table."""

    library = "$/custom/shadcn/table"
    tag = "TableRow"


class TableHead(HTMLThProps):
    """A header cell in a table."""

    library = "$/custom/shadcn/table"
    tag = "TableHead"


class TableCell(HTMLTdProps):
    """A cell in a table."""

    library = "$/custom/shadcn/table"
    tag = "TableCell"


class TableCaption(HTMLProps):
    """A caption for a table."""

    library = "$/custom/shadcn/table"
    tag = "TableCaption"


class TableNamespace(rx.ComponentNamespace):
    root = staticmethod(TableRoot.create)
    header = staticmethod(TableHeader.create)
    body = staticmethod(TableBody.create)
    footer = staticmethod(TableFooter.create)
    row = staticmethod(TableRow.create)
    head = staticmethod(TableHead.create)
    cell = staticmethod(TableCell.create)
    caption = staticmethod(TableCaption.create)


table = TableNamespace()


__all__ = [
    "TableRoot",
    "TableHeader",
    "TableBody",
    "TableFooter",
    "TableRow",
    "TableHead",
    "TableCell",
    "TableCaption",
    "table",
    "TableNamespace",
]
