from typing import Literal
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import GlobalAttributes, HTMLEventHandlersMixin


class Tabs(rx.Component, GlobalAttributes):
    """A tabs component based on shadcn/ui."""

    library = "$/custom/shadcn/tabs"
    tag = "Tabs"

    # Tabs specific props
    defaultValue: rx.Var[str] = rx.Var.create("")
    value: rx.Var[str] = rx.Var.create("")
    onValueChange: rx.EventHandler[lambda value: [value]]
    orientation: rx.Var[Literal["horizontal", "vertical"]] = rx.Var.create("horizontal")
    activationMode: rx.Var[Literal["automatic", "manual"]] = rx.Var.create("automatic")


class TabsList(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The list of tabs."""

    library = "$/custom/shadcn/tabs"
    tag = "TabsList"

    # TabsList specific props
    loop: rx.Var[bool] = rx.Var.create(True)


class TabsTrigger(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A tab trigger."""

    library = "$/custom/shadcn/tabs"
    tag = "TabsTrigger"

    # TabsTrigger specific props
    value: rx.Var[str] = rx.Var.create("")
    disabled: rx.Var[bool] = rx.Var.create(False)
    asChild: rx.Var[bool] = rx.Var.create(False)


class TabsContent(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """The content for a tab."""

    library = "$/custom/shadcn/tabs"
    tag = "TabsContent"

    # TabsContent specific props
    value: rx.Var[str] = rx.Var.create("")
    forceMount: rx.Var[bool] = rx.Var.create(False)
    asChild: rx.Var[bool] = rx.Var.create(False)


# Create helper functions


def tabs(*children, **props):
    """Create a Tabs component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Tabs.create(*children, **updated_props)


def tabs_list(*children, **props):
    """Create a TabsList component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return TabsList.create(*children, **updated_props)


def tabs_trigger(*children, **props):
    """Create a TabsTrigger component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return TabsTrigger.create(*children, **updated_props)


def tabs_content(*children, **props):
    """Create a TabsContent component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return TabsContent.create(*children, **updated_props)


__all__ = [
    "Tabs",
    "tabs",
    "TabsList",
    "tabs_list",
    "TabsTrigger",
    "tabs_trigger",
    "TabsContent",
    "tabs_content",
]
