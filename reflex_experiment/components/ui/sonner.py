from typing import Dict, Any, Literal, Optional, Union, List
import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from ..attributes import GlobalAttributes, HTMLEventHandlersMixin


class Toaster(rx.Component, GlobalAttributes):
    """A toast notification component based on sonner."""

    library = "$/custom/shadcn/sonner"
    tag = "Toaster"

    # Toaster specific props
    position: rx.Var[
        Literal[
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-center",
            "bottom-center",
        ]
    ] = rx.Var.create("bottom-right")
    hotkey: rx.Var[Union[List[str], str]] = rx.Var.create(["altKey", "KeyT"])
    richColors: rx.Var[bool] = rx.Var.create(False)
    expand: rx.Var[bool] = rx.Var.create(False)
    duration: rx.Var[int] = rx.Var.create(4000)
    visibleToasts: rx.Var[int] = rx.Var.create(3)
    closeButton: rx.Var[bool] = rx.Var.create(False)
    offset: rx.Var[Union[str, int]] = rx.Var.create("32px")
    theme: rx.Var[Literal["light", "dark", "system"]] = rx.Var.create("system")
    invert: rx.Var[bool] = rx.Var.create(False)
    style: rx.Var[Dict[str, Any]] = rx.Var.create({})
    className: rx.Var[str] = rx.Var.create("")
    toastOptions: rx.Var[Dict[str, Any]] = rx.Var.create({})
    gap: rx.Var[int] = rx.Var.create(14)
    loadingIcon: rx.Var[str] = rx.Var.create("")


class Toast(rx.Component, GlobalAttributes, HTMLEventHandlersMixin):
    """A toast component to be used with the Toaster."""

    library = "$/custom/shadcn/sonner"
    tag = "Toast"

    # Toast specific props
    id: rx.Var[str] = rx.Var.create("")
    title: rx.Var[str] = rx.Var.create("")
    description: rx.Var[str] = rx.Var.create("")
    type: rx.Var[
        Literal["default", "success", "info", "warning", "error", "loading"]
    ] = rx.Var.create("default")
    duration: rx.Var[int] = rx.Var.create(4000)
    icon: rx.Var[str] = rx.Var.create("")
    action: rx.Var[Dict[str, Any]] = rx.Var.create({})
    cancel: rx.Var[Dict[str, Any]] = rx.Var.create({})
    onDismiss: rx.EventHandler[lambda toast: [toast]]
    onAutoClose: rx.EventHandler[lambda toast: [toast]]
    dismissible: rx.Var[bool] = rx.Var.create(True)
    position: rx.Var[
        Literal[
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-center",
            "bottom-center",
        ]
    ] = rx.Var.create("bottom-right")
    invert: rx.Var[bool] = rx.Var.create(False)
    important: rx.Var[bool] = rx.Var.create(False)
    style: rx.Var[Dict[str, Any]] = rx.Var.create({})
    className: rx.Var[str] = rx.Var.create("")


# Create helper functions


def toaster(*children, **props):
    """Create a Toaster component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Toaster.create(*children, **updated_props)


def toast(*children, **props):
    """Create a Toast component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Toast.create(*children, **updated_props)


__all__ = [
    "Toaster",
    "toaster",
    "Toast",
    "toast",
]
