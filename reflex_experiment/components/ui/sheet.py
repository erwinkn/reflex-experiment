from typing import Optional, Literal
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import GlobalAttributes, HTMLEventHandlersMixin


class Sheet(rx.Component, GlobalAttributes):
    """A sheet component."""

    library = "$/custom/shadcn/sheet"
    tag = "Sheet"

    # Sheet specific props
    defaultOpen: rx.Var[bool] = rx.Var.create(False)
    open: rx.Var[bool] = rx.Var.create(False)
    onOpenChange: rx.EventHandler[lambda open: [open]]
    modal: rx.Var[bool] = rx.Var.create(True)
    side: rx.Var[Literal["top", "right", "bottom", "left"]] = rx.Var.create("right")


class SheetTrigger(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A button that triggers the sheet."""

    library = "$/custom/shadcn/sheet"
    tag = "SheetTrigger"

    # SheetTrigger specific props
    asChild: rx.Var[bool] = rx.Var.create(False)


class SheetClose(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A button to close the sheet."""

    library = "$/custom/shadcn/sheet"
    tag = "SheetClose"

    # SheetClose specific props
    asChild: rx.Var[bool] = rx.Var.create(False)


class SheetPortal(rx.Component, GlobalAttributes):
    """A portal for the sheet content."""

    library = "$/custom/shadcn/sheet"
    tag = "SheetPortal"

    # SheetPortal specific props
    forceMount: rx.Var[bool] = rx.Var.create(False)
    container: rx.Var[str] = rx.Var.create("")


class SheetOverlay(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The overlay for the sheet."""

    library = "$/custom/shadcn/sheet"
    tag = "SheetOverlay"

    # SheetOverlay specific props
    forceMount: rx.Var[bool] = rx.Var.create(False)


class SheetContent(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The content of the sheet."""

    library = "$/custom/shadcn/sheet"
    tag = "SheetContent"

    # SheetContent specific props
    forceMount: rx.Var[bool] = rx.Var.create(False)
    side: rx.Var[Literal["top", "right", "bottom", "left"]] = rx.Var.create("right")
    onEscapeKeyDown: rx.EventHandler[lambda event: [event]]
    onPointerDownOutside: rx.EventHandler[lambda event: [event]]
    onInteractOutside: rx.EventHandler[lambda event: [event]]


class SheetHeader(rx.Component, GlobalAttributes):
    """The header of the sheet."""

    library = "$/custom/shadcn/sheet"
    tag = "SheetHeader"


class SheetFooter(rx.Component, GlobalAttributes):
    """The footer of the sheet."""

    library = "$/custom/shadcn/sheet"
    tag = "SheetFooter"


class SheetTitle(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The title of the sheet."""

    library = "$/custom/shadcn/sheet"
    tag = "SheetTitle"

    # SheetTitle specific props
    asChild: rx.Var[bool] = rx.Var.create(False)


class SheetDescription(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The description of the sheet."""

    library = "$/custom/shadcn/sheet"
    tag = "SheetDescription"

    # SheetDescription specific props
    asChild: rx.Var[bool] = rx.Var.create(False)


# Create helper functions


def sheet(*children, **props):
    """Create a Sheet component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Sheet.create(*children, **updated_props)


def sheet_trigger(*children, **props):
    """Create a SheetTrigger component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return SheetTrigger.create(*children, **updated_props)


def sheet_close(*children, **props):
    """Create a SheetClose component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return SheetClose.create(*children, **updated_props)


def sheet_portal(*children, **props):
    """Create a SheetPortal component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return SheetPortal.create(*children, **updated_props)


def sheet_overlay(*children, **props):
    """Create a SheetOverlay component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return SheetOverlay.create(*children, **updated_props)


def sheet_content(*children, **props):
    """Create a SheetContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return SheetContent.create(*children, **updated_props)


def sheet_header(*children, **props):
    """Create a SheetHeader component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return SheetHeader.create(*children, **updated_props)


def sheet_footer(*children, **props):
    """Create a SheetFooter component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return SheetFooter.create(*children, **updated_props)


def sheet_title(*children, **props):
    """Create a SheetTitle component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return SheetTitle.create(*children, **updated_props)


def sheet_description(*children, **props):
    """Create a SheetDescription component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return SheetDescription.create(*children, **updated_props)


__all__ = [
    "Sheet",
    "sheet",
    "SheetTrigger",
    "sheet_trigger",
    "SheetClose",
    "sheet_close",
    "SheetPortal",
    "sheet_portal",
    "SheetOverlay",
    "sheet_overlay",
    "SheetContent",
    "sheet_content",
    "SheetHeader",
    "sheet_header",
    "SheetFooter",
    "sheet_footer",
    "SheetTitle",
    "sheet_title",
    "SheetDescription",
    "sheet_description",
]
