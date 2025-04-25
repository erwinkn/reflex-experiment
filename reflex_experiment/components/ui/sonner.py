from typing import Dict, Any, Literal, Optional, Union, List
import reflex as rx
from reflex_experiment.attributes import HTMLProps

#TODO:
# - Verify that snake_case -> camelCase works for nested objects
class ToastOptions(rx.Base):
    class_name: Optional[str] = None
    close_button: Optional[bool] = None
    description_class_name: Optional[str] = None
    style: Optional[Dict[str, Any]] = None
    cancel_button_style: Optional[Dict[str, Any]] = None
    action_button_style: Optional[Dict[str, Any]] = None
    duration: Optional[int] = None
    unstyled: Optional[bool] = None
    class_names: Optional[Dict[str, str]] = None
    close_button_aria_label: Optional[str] = None

class OffsetObject(rx.Base):
    top: str | float | None = None
    right: str | float | None = None
    bottom: str | float | None = None
    left: str | float | None = None

class Toaster(HTMLProps):
    """A toast notification component based on sonner."""

    library = "$/custom/shadcn/sonner"
    tag = "Toaster"

    invert: rx.Var[bool]
    theme: rx.Var[Literal["light", "dark", "system"]]
    position: rx.Var[Literal['top-left', 'top-right', 'bottom-left', 'bottom-right', 'top-center', 'bottom-center']]  # Position type
    hotkey: rx.Var[List[str]]
    rich_colors: rx.Var[bool]
    expand: rx.Var[bool]
    duration: rx.Var[int]
    gap: rx.Var[int]
    visible_toasts: rx.Var[int]
    close_button: rx.Var[bool]
    toast_options: ToastOptions
    offset: rx.Var[Union[Dict[str, Union[str, int]], str, int]]  # Offset type
    mobile_offset: rx.Var[Union[Dict[str, Union[str, int]], str, int]]  # Offset type
    swipe_directions: rx.Var[List[str]]  # SwipeDirection[] type
    icons: rx.Var[Dict[str, Any]]  # ToastIcons type
    container_aria_label: rx.Var[str]


toaster = Toaster.create


__all__ = [
    "Toaster",
    "toaster",
]
