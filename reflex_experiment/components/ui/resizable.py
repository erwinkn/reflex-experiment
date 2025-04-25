from typing import Literal
import reflex as rx
from reflex_experiment.attributes import HTMLProps
from reflex_experiment.helpers import TypedEventHandler


# Can be any element, depending on the tag_name prop
class ResizablePanelGroup(HTMLProps):
    """A group of resizable panels."""

    library = "$/custom/shadcn/resizable"
    tag = "ResizablePanelGroup"

    # ResizablePanelGroup specific props
    auto_save_id: rx.Var[str]
    direction: rx.Var[Literal['horizontal', 'vertical']] = rx.Var.create("horizontal")
    keyboard_resize_by: rx.Var[float]
    # (layout: number[]) => void
    on_layout: TypedEventHandler[list[float]]
    # storage -> omitted, it's a way to pass callbacks
    tag_name: str



# Can be any element, depending on the tag_name prop
class ResizablePanel(HTMLProps):
    """A resizable panel component."""

    library = "$/custom/shadcn/resizable"
    tag = "ResizablePanel"

    # ResizablePanel specific props
    collapsed_size: rx.Var[float]
    collapsible: rx.Var[bool]
    default_size: rx.Var[float]
    max_size: rx.Var[float]
    min_size: rx.Var[float]
    on_collapse: TypedEventHandler[None]
    on_expand: TypedEventHandler[None]
    # (size: number, prevSize: number | undefined) => void
    on_resize: TypedEventHandler[float, float | None]
    order: rx.Var[float]
    tag_name: str


class PointerHitAreaMargins(rx.Base):
    coarse: float
    fine: float


# Can be any element, depending on the tag_name prop
class ResizableHandle(HTMLProps):
    """A handle for resizing panels."""

    library = "$/custom/shadcn/resizable"
    tag = "ResizableHandle"

    # ResizableHandle specific props
    with_handle: rx.Var[bool]
    hit_area_margins: rx.Var[PointerHitAreaMargins]

    on_blur: TypedEventHandler[None]
    on_dragging: TypedEventHandler[bool]  # (isDragging: boolean) => void
    on_focus: TypedEventHandler[None]
    tag_name: rx.Var[str]


class ResizableNamespace(rx.ComponentNamespace):
    panel_group = staticmethod(ResizablePanelGroup.create)
    panel = staticmethod(ResizablePanel.create)
    handle = staticmethod(ResizableHandle.create)


resizable = ResizableNamespace()


__all__ = [
    "ResizablePanelGroup",
    "ResizablePanel", 
    "ResizableHandle",
    "resizable",
    "ResizableNamespace",
]
