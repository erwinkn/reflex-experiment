import reflex as rx
from reflex_experiment.attributes import HTMLProps, HTMLButtonProps
from reflex_experiment.helpers import TypedEventHandler


class CollapsibleRoot(HTMLProps):
    """A collapsible component that can be opened and closed."""

    library = "$/custom/shadcn/collapsible"
    tag = "Collapsible"

    # Collapsible specific props
    as_child: rx.Var[bool]
    default_open: rx.Var[bool]
    open: rx.Var[bool]
    on_open_change: TypedEventHandler[bool]
    disabled: rx.Var[bool]


class CollapsibleTrigger(HTMLButtonProps):
    """A button that triggers the collapsible component to open or close."""

    library = "$/custom/shadcn/collapsible"
    tag = "CollapsibleTrigger"

    # CollapsibleTrigger specific props
    as_child: rx.Var[bool]


class CollapsibleContent(HTMLProps):
    """The content of the collapsible component that gets shown or hidden."""

    library = "$/custom/shadcn/collapsible"
    tag = "CollapsibleContent"

    # CollapsibleContent specific props
    as_child: rx.Var[bool]
    force_mount: rx.Var[bool]


class CollapsibleNamespace(rx.ComponentNamespace):
    root = staticmethod(CollapsibleRoot.create)
    trigger = staticmethod(CollapsibleTrigger.create)
    content = staticmethod(CollapsibleContent.create)


collapsible = CollapsibleNamespace()


__all__ = [
    "CollapsibleRoot",
    "CollapsibleTrigger",
    "CollapsibleContent",
    "collapsible",
    "CollapsibleNamespace",
]
