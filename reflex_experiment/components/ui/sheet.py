from typing import Literal
import reflex as rx
from reflex_experiment.attributes import HTMLProps, HTMLButtonProps
from reflex_experiment.elements import HTMLElement
from reflex_experiment.events import KeyboardEvent, PointerEvent, SyntheticEvent
from reflex_experiment.helpers import TypedEventHandler


class SheetRoot(HTMLProps):
    """A sheet component."""

    library = "$/custom/shadcn/sheet"
    tag = "Sheet"

    # Sheet specific props
    default_open: rx.Var[bool]
    open: rx.Var[bool]
    on_open_change: TypedEventHandler[bool]
    modal: rx.Var[bool]
    side: rx.Var[Literal["top", "right", "bottom", "left"]]


class SheetTrigger(HTMLButtonProps):
    """A button that triggers the sheet."""

    library = "$/custom/shadcn/sheet"
    tag = "SheetTrigger"

    # SheetTrigger specific props
    as_child: rx.Var[bool]


class SheetClose(HTMLButtonProps):
    """A button to close the sheet."""

    library = "$/custom/shadcn/sheet"
    tag = "SheetClose"

    # SheetClose specific props
    as_child: rx.Var[bool]


class SheetPortal(HTMLProps):
    """A portal for the sheet content."""

    library = "$/custom/shadcn/sheet"
    tag = "SheetPortal"

    # SheetPortal specific props
    force_mount: rx.Var[bool]
    container: rx.Var[str]


class SheetOverlay(HTMLProps):
    """The overlay for the sheet."""

    library = "$/custom/shadcn/sheet"
    tag = "SheetOverlay"

    # SheetOverlay specific props
    force_mount: rx.Var[bool]


class SheetContent(HTMLProps):
    """The content of the sheet."""

    library = "$/custom/shadcn/sheet"
    tag = "SheetContent"

    # SheetContent specific props
    force_mount: rx.Var[bool]
    side: rx.Var[Literal["top", "right", "bottom", "left"]]
    on_escape_key_down: TypedEventHandler[KeyboardEvent[HTMLElement]]
    on_pointer_down_outside: TypedEventHandler[PointerEvent[HTMLElement]]
    # Real signature: (event: React.FocusEvent | MouseEvent | TouchEvent) => void
    on_interact_outside: TypedEventHandler[SyntheticEvent[HTMLElement]]


class SheetHeader(HTMLProps):
    """The header of the sheet."""

    library = "$/custom/shadcn/sheet"
    tag = "SheetHeader"


class SheetFooter(HTMLProps):
    """The footer of the sheet."""

    library = "$/custom/shadcn/sheet"
    tag = "SheetFooter"


class SheetTitle(HTMLProps):
    """The title of the sheet."""

    library = "$/custom/shadcn/sheet"
    tag = "SheetTitle"

    # SheetTitle specific props
    as_child: rx.Var[bool]


class SheetDescription(HTMLProps):
    """The description of the sheet."""

    library = "$/custom/shadcn/sheet"
    tag = "SheetDescription"

    # SheetDescription specific props
    as_child: rx.Var[bool]


class SheetNamespace(rx.ComponentNamespace):
    root = staticmethod(SheetRoot.create)
    trigger = staticmethod(SheetTrigger.create)
    close = staticmethod(SheetClose.create)
    portal = staticmethod(SheetPortal.create)
    overlay = staticmethod(SheetOverlay.create)
    content = staticmethod(SheetContent.create)
    header = staticmethod(SheetHeader.create)
    footer = staticmethod(SheetFooter.create)
    title = staticmethod(SheetTitle.create)
    description = staticmethod(SheetDescription.create)


sheet = SheetNamespace()


__all__ = [
    "SheetRoot",
    "SheetTrigger",
    "SheetClose",
    "SheetPortal",
    "SheetOverlay",
    "SheetContent",
    "SheetHeader",
    "SheetFooter",
    "SheetTitle",
    "SheetDescription",
    "sheet",
    "SheetNamespace",
]
