from typing import Literal
import reflex as rx
from reflex_experiment.attributes import HTMLProps, HTMLButtonProps
from reflex_experiment.helpers import TypedEventHandler


class TabsRoot(HTMLProps):
    """A tabs component based on shadcn/ui."""

    library = "$/custom/shadcn/tabs"
    tag = "Tabs"

    # Tabs specific props
    default_value: rx.Var[str]
    value: rx.Var[str]
    on_value_change: TypedEventHandler[str]
    orientation: rx.Var[Literal["horizontal", "vertical"]]
    activation_mode: rx.Var[Literal["automatic", "manual"]]


class TabsList(HTMLProps):
    """The list of tabs."""

    library = "$/custom/shadcn/tabs"
    tag = "TabsList"

    # TabsList specific props
    loop: rx.Var[bool]


class TabsTrigger(HTMLButtonProps):
    """A tab trigger."""

    library = "$/custom/shadcn/tabs"
    tag = "TabsTrigger"

    # TabsTrigger specific props
    value: rx.Var[str]
    disabled: rx.Var[bool]
    as_child: rx.Var[bool]


class TabsContent(HTMLProps):
    """The content for a tab."""

    library = "$/custom/shadcn/tabs"
    tag = "TabsContent"

    # TabsContent specific props
    value: rx.Var[str]
    force_mount: rx.Var[bool]
    as_child: rx.Var[bool]


class TabsNamespace(rx.ComponentNamespace):
    root = staticmethod(TabsRoot.create)
    list = staticmethod(TabsList.create)
    trigger = staticmethod(TabsTrigger.create)
    content = staticmethod(TabsContent.create)


tabs = TabsNamespace()


__all__ = [
    "TabsRoot",
    "TabsList",
    "TabsTrigger",
    "TabsContent",
    "tabs",
    "TabsNamespace",
]
