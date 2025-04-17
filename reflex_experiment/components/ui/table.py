from typing import Literal
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import GlobalAttributes, HTMLEventHandlersMixin


class Table(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A table component based on shadcn/ui."""

    library = "$/custom/shadcn/table"
    tag = "Table"


class TableHeader(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The header of a table."""

    library = "$/custom/shadcn/table"
    tag = "TableHeader"


class TableBody(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The body of a table."""

    library = "$/custom/shadcn/table"
    tag = "TableBody"


class TableFooter(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The footer of a table."""

    library = "$/custom/shadcn/table"
    tag = "TableFooter"


class TableRow(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A row in a table."""

    library = "$/custom/shadcn/table"
    tag = "TableRow"


class TableHead(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A header cell in a table."""

    library = "$/custom/shadcn/table"
    tag = "TableHead"


class TableCell(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A cell in a table."""

    library = "$/custom/shadcn/table"
    tag = "TableCell"


class TableCaption(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A caption for a table."""

    library = "$/custom/shadcn/table"
    tag = "TableCaption"


# Create helper functions


def table(*children, **props):
    """Create a Table component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Table.create(*children, **updated_props)


def table_header(*children, **props):
    """Create a TableHeader component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return TableHeader.create(*children, **updated_props)


def table_body(*children, **props):
    """Create a TableBody component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return TableBody.create(*children, **updated_props)


def table_footer(*children, **props):
    """Create a TableFooter component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return TableFooter.create(*children, **updated_props)


def table_row(*children, **props):
    """Create a TableRow component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return TableRow.create(*children, **updated_props)


def table_head(*children, **props):
    """Create a TableHead component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return TableHead.create(*children, **updated_props)


def table_cell(*children, **props):
    """Create a TableCell component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return TableCell.create(*children, **updated_props)


def table_caption(*children, **props):
    """Create a TableCaption component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return TableCaption.create(*children, **updated_props)


__all__ = [
    "Table",
    "table",
    "TableHeader",
    "table_header",
    "TableBody",
    "table_body",
    "TableFooter",
    "table_footer",
    "TableRow",
    "table_row",
    "TableHead",
    "table_head",
    "TableCell",
    "table_cell",
    "TableCaption",
    "table_caption",
]
