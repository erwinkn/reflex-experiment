from typing import List, Optional, Union, Dict, Any
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import GlobalAttributes, HTMLEventHandlersMixin


class ResizablePanelGroup(rx.Component, GlobalAttributes):
    """A group of resizable panels."""

    library = "$/custom/shadcn/resizable"
    tag = "ResizablePanelGroup"

    # ResizablePanelGroup specific props
    direction: rx.Var[str] = rx.Var.create("horizontal")
    onLayout: rx.EventHandler[lambda sizes: [sizes]]


class ResizablePanel(rx.Component, GlobalAttributes):
    """A resizable panel component."""

    library = "$/custom/shadcn/resizable"
    tag = "ResizablePanel"

    # ResizablePanel specific props
    defaultSize: rx.Var[int] = rx.Var.create(0)
    size: rx.Var[int] = rx.Var.create(0)
    onResize: rx.EventHandler[lambda size: [size]]
    minSize: rx.Var[int] = rx.Var.create(0)
    maxSize: rx.Var[int] = rx.Var.create(100)
    collapsible: rx.Var[bool] = rx.Var.create(False)
    collapsedSize: rx.Var[int] = rx.Var.create(0)
    className: rx.Var[str] = rx.Var.create("")
    style: rx.Var[Dict[str, Any]] = rx.Var.create({})


class ResizableHandle(rx.Component, GlobalAttributes):
    """A handle for resizing panels."""

    library = "$/custom/shadcn/resizable"
    tag = "ResizableHandle"

    # ResizableHandle specific props
    withHandle: rx.Var[bool] = rx.Var.create(False)
    className: rx.Var[str] = rx.Var.create("")
    style: rx.Var[Dict[str, Any]] = rx.Var.create({})


# Create helper functions


def resizable_panel_group(*children, **props):
    """Create a ResizablePanelGroup component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ResizablePanelGroup.create(*children, **updated_props)


def resizable_panel(*children, **props):
    """Create a ResizablePanel component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ResizablePanel.create(*children, **updated_props)


def resizable_handle(*children, **props):
    """Create a ResizableHandle component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return ResizableHandle.create(*children, **updated_props)


__all__ = [
    "ResizablePanelGroup",
    "resizable_panel_group",
    "ResizablePanel",
    "resizable_panel",
    "ResizableHandle",
    "resizable_handle",
]
