# Adapted from @types/react 19.0
# Notes:
# - We cannot serialize or use any methods on event objects or their targets
# - We can only serialize data
# - This makes the EventTarget type effectively empty

from typing import (
    Callable,
    Literal,
    Generic,
    TypeVar,
    Optional,
    TypedDict,
    cast,
)
import reflex as rx
from reflex.vars import var_operation, var_operation_return, VarData
from reflex.utils.imports import ImportVar
from pydantic.v1 import BaseModel, Field
from pydantic.v1.generics import GenericModel

# Import base element type and specific elements if needed for defaults or bounds
from .elements import (
    HTMLElementField,
    HTMLElement,
    HTMLElementBase,
    HTMLInputElement,
    HTMLSelectElement,
    HTMLTextAreaElement,  # Import the Union type
)  # Example imports


# Generic TypeVar for the element target
TElement = TypeVar("TElement", bound=HTMLElementBase)
TRelatedTarget = TypeVar(
    "TRelatedTarget", bound=HTMLElementBase
)  # relatedTarget can be null


class DataTransferItem(BaseModel):
    kind: str
    type: str


class DataTransfer(BaseModel):
    drop_effect: Literal["none", "copy", "link", "move"]
    effect_allowed: Literal[
        "none",
        "copy",
        "copyLink",
        "copyMove",
        "link",
        "linkMove",
        "move",
        "all",
        "uninitialized",
    ]
    # files: Any  # FileList equivalent
    items: list[DataTransferItem]  # DataTransferItemList
    types: list[str]


class Touch(BaseModel):
    target: HTMLElement = HTMLElementField
    identifier: int
    screen_x: float
    screen_y: float
    client_x: float
    client_y: float
    page_x: float
    page_y: float


# Base SyntheticEvent using rx.Base and Generic
class SyntheticEvent(GenericModel, Generic[TElement]):
    # nativeEvent: Any # Omitted
    # current_target: TElement  # element on which the event listener is registered
    target: HTMLElement  # target of the event (may be a child)
    bubbles: bool
    cancelable: bool
    default_prevented: bool
    event_phase: int
    is_trusted: bool
    # preventDefault(): void;
    # isDefaultPrevented(): boolean;
    # stopPropagation(): void;
    # isPropagationStopped(): boolean;
    # persist(): void;
    timestamp: int
    type: str


class UIEvent(SyntheticEvent, Generic[TElement]):
    detail: int
    # view: Any # AbstractView - Omitted


class MouseEvent(UIEvent, Generic[TElement]):
    alt_key: bool
    button: int
    buttons: int
    client_x: float
    client_y: float
    ctrl_key: bool
    # getModifierState(key: ModifierKey): boolean
    meta_key: bool
    movement_x: float
    movement_y: float
    page_x: float
    page_y: float
    related_target: Optional[HTMLElement] = HTMLElementField
    screen_x: float
    screen_y: float
    shift_key: bool


class ClipboardEvent(SyntheticEvent, Generic[TElement]):
    clipboard_data: DataTransfer


class CompositionEvent(SyntheticEvent, Generic[TElement]):
    data: str


class DragEvent(MouseEvent, Generic[TElement]):
    data_transfer: DataTransfer


class PointerEvent(MouseEvent, Generic[TElement]):
    pointer_id: int
    pressure: float
    tangential_pressure: float
    tilt_x: float
    tilt_y: float
    twist: float
    width: float
    height: float
    pointer_type: Literal["mouse", "pen", "touch"]
    is_primary: bool


class FocusEvent(
    SyntheticEvent,
    Generic[TElement],
):
    target: TElement
    related_target: Optional[HTMLElement] = (
        HTMLElementField  # (EventTarget & RelatedTarget) | null
    )


class FormEvent(SyntheticEvent, Generic[TElement]):
    # No specific fields added here
    pass


class InvalidEvent(SyntheticEvent, Generic[TElement]):
    target: TElement


class ChangeEvent(SyntheticEvent, Generic[TElement]):
    target: TElement


ModifierKey = Literal[
    "Alt",
    "AltGraph",
    "CapsLock",
    "Control",
    "Fn",
    "FnLock",
    "Hyper",
    "Meta",
    "NumLock",
    "ScrollLock",
    "Shift",
    "Super",
    "Symbol",
    "SymbolLock",
]


class KeyboardEvent(UIEvent, Generic[TElement]):
    alt_key: bool
    # char_code: int  # deprecated
    ctrl_key: bool
    code: str
    # getModifierState(key: ModifierKey): boolean
    key: str
    # key_code: int  # deprecated
    locale: str
    location: int
    meta_key: bool
    repeat: bool
    shift_key: bool
    # which: int  # deprecated


class TouchEvent(UIEvent, Generic[TElement]):
    alt_key: bool
    changed_touches: list[Touch]  # TouchList
    ctrl_key: bool
    # getModifierState(key: ModifierKey): boolean
    meta_key: bool
    shift_key: bool
    target_touches: list[Touch]  # TouchList
    touches: list[Touch]  # TouchList


class WheelEvent(MouseEvent, Generic[TElement]):
    delta_mode: int
    delta_x: float
    delta_y: float
    delta_z: float


class AnimationEvent(SyntheticEvent, Generic[TElement]):
    animation_name: str
    elapsed_time: float
    pseudo_element: str


class ToggleEvent(SyntheticEvent, Generic[TElement]):
    old_state: Literal["closed", "open"]
    new_state: Literal["closed", "open"]


class TransitionEvent(SyntheticEvent, Generic[TElement]):
    elapsed_time: float
    property_name: str
    pseudo_element: str


@var_operation
def handle_event_operation(var: rx.Var, fn: str):
    """Applies the custom cleanForSerialization JS function to the input Var."""
    custom_import = {"$/custom/serialize": [ImportVar(tag="cleanForSerialization")]}
    fn = "extract" + fn
    return var_operation_return(
        js_expression=f"{fn}({var})",
        var_data=VarData(imports=custom_import),
    )


TType = TypeVar("TType", bound=type)


def make_handler(fn: str, return_type: TType):  # type: ignore
    def handle_event(var: rx.Var) -> tuple[rx.Var[return_type]]:
        return (handle_event_operation(var, fn),)

    return handle_event


def DOMEvents(t_element: type[TElement]):
    generic_handler = make_handler("SyntheticEvent", SyntheticEvent[t_element])
    ui_handler = make_handler("UIEvent", UIEvent[t_element])
    clipboard_handler = make_handler("ClipboardEvent", ClipboardEvent[t_element])
    composition_handler = make_handler("CompositionEvent", CompositionEvent[t_element])
    drag_handler = make_handler("DragEvent", DragEvent[t_element])
    pointer_handler = make_handler("PointerEvent", PointerEvent[t_element])
    focus_handler = make_handler("FocusEvent", FocusEvent[t_element])
    form_handler = make_handler("FormEvent", FormEvent[t_element])
    keyboard_handler = make_handler("KeyboardEvent", KeyboardEvent[t_element])
    mouse_handler = make_handler("MouseEvent", MouseEvent[t_element])
    touch_handler = make_handler("TouchEvent", TouchEvent[t_element])
    wheel_handler = make_handler("WheelEvent", WheelEvent[t_element])
    animation_handler = make_handler("AnimationEvent", AnimationEvent[t_element])
    toggle_handler = make_handler("ToggleEvent", ToggleEvent[t_element])
    transition_handler = make_handler("TransitionEvent", TransitionEvent[t_element])
    # More specific type for these three elements, where `target` is always the element itself
    if t_element in (HTMLInputElement, HTMLTextAreaElement, HTMLSelectElement):
        change_handler = make_handler("ChangeEvent", ChangeEvent[t_element])
    else:
        change_handler = make_handler("FocusEvent", FocusEvent[t_element])

    class DOMEventsMixin(rx.Component):
        # Clipboard Events
        on_copy: rx.EventHandler[clipboard_handler]
        on_copy_capture: rx.EventHandler[clipboard_handler]
        on_cut: rx.EventHandler[clipboard_handler]
        on_cut_capture: rx.EventHandler[clipboard_handler]
        on_paste: rx.EventHandler[clipboard_handler]
        on_paste_capture: rx.EventHandler[clipboard_handler]

        # Composition Events
        on_composition_end: rx.EventHandler[composition_handler]
        on_composition_end_capture: rx.EventHandler[composition_handler]
        on_composition_start: rx.EventHandler[composition_handler]
        on_composition_start_capture: rx.EventHandler[composition_handler]
        on_composition_update: rx.EventHandler[composition_handler]
        on_composition_update_capture: rx.EventHandler[composition_handler]

        # Focus Events
        on_focus: rx.EventHandler[focus_handler]
        on_focus_capture: rx.EventHandler[focus_handler]
        on_blur: rx.EventHandler[focus_handler]
        on_blur_capture: rx.EventHandler[focus_handler]

        # Form Events
        # Special typing for on_change for <input>, <textarea>, and <select> elements
        on_change: rx.EventHandler[change_handler]
        on_change_capture: rx.EventHandler[form_handler]
        on_before_input: rx.EventHandler[form_handler]  # FormEvent is often used
        on_before_input_capture: rx.EventHandler[form_handler]
        on_input: rx.EventHandler[form_handler]  # FormEvent is often used
        on_input_capture: rx.EventHandler[form_handler]
        on_reset: rx.EventHandler[form_handler]
        on_reset_capture: rx.EventHandler[form_handler]
        on_submit: rx.EventHandler[form_handler]
        on_submit_capture: rx.EventHandler[form_handler]
        on_invalid: rx.EventHandler[form_handler]
        on_invalid_capture: rx.EventHandler[form_handler]

        # Image Events (Usually SyntheticEvent)
        on_load: rx.EventHandler[generic_handler]
        on_load_capture: rx.EventHandler[generic_handler]
        on_error: rx.EventHandler[generic_handler]  # also a Media Event
        on_error_capture: rx.EventHandler[generic_handler]  # also a Media Event

        # Keyboard Events
        on_key_down: rx.EventHandler[keyboard_handler]
        on_key_down_capture: rx.EventHandler[keyboard_handler]
        # on_key_press: rx.EventHandler[keyboard_handler] # deprecated
        # on_key_press_capture: rx.EventHandler[keyboard_handler] # deprecated
        on_key_up: rx.EventHandler[keyboard_handler]
        on_key_up_capture: rx.EventHandler[keyboard_handler]

        # Media Events (Usually SyntheticEvent)
        on_abort: rx.EventHandler[generic_handler]
        on_abort_capture: rx.EventHandler[generic_handler]
        on_can_play: rx.EventHandler[generic_handler]
        on_can_play_capture: rx.EventHandler[generic_handler]
        on_can_play_through: rx.EventHandler[generic_handler]
        on_can_play_through_capture: rx.EventHandler[generic_handler]
        on_duration_change: rx.EventHandler[generic_handler]
        on_duration_change_capture: rx.EventHandler[generic_handler]
        on_emptied: rx.EventHandler[generic_handler]
        on_emptied_capture: rx.EventHandler[generic_handler]
        on_encrypted: rx.EventHandler[generic_handler]
        on_encrypted_capture: rx.EventHandler[generic_handler]
        on_ended: rx.EventHandler[generic_handler]
        on_ended_capture: rx.EventHandler[generic_handler]
        on_loaded_data: rx.EventHandler[generic_handler]
        on_loaded_data_capture: rx.EventHandler[generic_handler]
        on_loaded_metadata: rx.EventHandler[generic_handler]
        on_loaded_metadata_capture: rx.EventHandler[generic_handler]
        on_load_start: rx.EventHandler[generic_handler]
        on_load_start_capture: rx.EventHandler[generic_handler]
        on_pause: rx.EventHandler[generic_handler]
        on_pause_capture: rx.EventHandler[generic_handler]
        on_play: rx.EventHandler[generic_handler]
        on_play_capture: rx.EventHandler[generic_handler]
        on_playing: rx.EventHandler[generic_handler]
        on_playing_capture: rx.EventHandler[generic_handler]
        on_progress: rx.EventHandler[generic_handler]
        on_progress_capture: rx.EventHandler[generic_handler]
        on_rate_change: rx.EventHandler[generic_handler]
        on_rate_change_capture: rx.EventHandler[generic_handler]
        on_resize: rx.EventHandler[generic_handler]
        on_resize_capture: rx.EventHandler[generic_handler]
        on_seeked: rx.EventHandler[generic_handler]
        on_seeked_capture: rx.EventHandler[generic_handler]
        on_seeking: rx.EventHandler[generic_handler]
        on_seeking_capture: rx.EventHandler[generic_handler]
        on_stalled: rx.EventHandler[generic_handler]
        on_stalled_capture: rx.EventHandler[generic_handler]
        on_suspend: rx.EventHandler[generic_handler]
        on_suspend_capture: rx.EventHandler[generic_handler]
        on_time_update: rx.EventHandler[generic_handler]
        on_time_update_capture: rx.EventHandler[generic_handler]
        on_volume_change: rx.EventHandler[generic_handler]
        on_volume_change_capture: rx.EventHandler[generic_handler]
        on_waiting: rx.EventHandler[generic_handler]
        on_waiting_capture: rx.EventHandler[generic_handler]

        # Mouse Events (Using pointer_event for consistency where applicable, mouse_event otherwise)
        on_aux_click: rx.EventHandler[mouse_handler]
        on_aux_click_capture: rx.EventHandler[mouse_handler]
        on_click: rx.EventHandler[mouse_handler]  # Often PointerEvent in modern React
        on_click_capture: rx.EventHandler[mouse_handler]
        on_context_menu: rx.EventHandler[mouse_handler]
        on_context_menu_capture: rx.EventHandler[mouse_handler]
        on_double_click: rx.EventHandler[mouse_handler]
        on_double_click_capture: rx.EventHandler[mouse_handler]

        on_drag: rx.EventHandler[drag_handler]
        on_drag_capture: rx.EventHandler[drag_handler]
        on_drag_end: rx.EventHandler[drag_handler]
        on_drag_end_capture: rx.EventHandler[drag_handler]
        on_drag_enter: rx.EventHandler[drag_handler]
        on_drag_enter_capture: rx.EventHandler[drag_handler]
        on_drag_exit: rx.EventHandler[drag_handler]
        on_drag_exit_capture: rx.EventHandler[drag_handler]
        on_drag_leave: rx.EventHandler[drag_handler]
        on_drag_leave_capture: rx.EventHandler[drag_handler]
        on_drag_over: rx.EventHandler[drag_handler]
        on_drag_over_capture: rx.EventHandler[drag_handler]
        on_drag_start: rx.EventHandler[drag_handler]
        on_drag_start_capture: rx.EventHandler[drag_handler]
        on_drop: rx.EventHandler[drag_handler]
        on_drop_capture: rx.EventHandler[drag_handler]

        on_mouse_down: rx.EventHandler[mouse_handler]
        on_mouse_down_capture: rx.EventHandler[mouse_handler]
        on_mouse_enter: rx.EventHandler[mouse_handler]  # Uses MouseEvent
        on_mouse_leave: rx.EventHandler[mouse_handler]  # Uses MouseEvent
        on_mouse_move: rx.EventHandler[mouse_handler]
        on_mouse_move_capture: rx.EventHandler[mouse_handler]
        on_mouse_out: rx.EventHandler[mouse_handler]
        on_mouse_out_capture: rx.EventHandler[mouse_handler]
        on_mouse_over: rx.EventHandler[mouse_handler]
        on_mouse_over_capture: rx.EventHandler[mouse_handler]
        on_mouse_up: rx.EventHandler[mouse_handler]
        on_mouse_up_capture: rx.EventHandler[mouse_handler]

        # Selection Events (Usually SyntheticEvent)
        on_select: rx.EventHandler[generic_handler]
        on_select_capture: rx.EventHandler[generic_handler]

        # Touch Events
        on_touch_cancel: rx.EventHandler[touch_handler]
        on_touch_cancel_capture: rx.EventHandler[touch_handler]
        on_touch_end: rx.EventHandler[touch_handler]
        on_touch_end_capture: rx.EventHandler[touch_handler]
        on_touch_move: rx.EventHandler[touch_handler]
        on_touch_move_capture: rx.EventHandler[touch_handler]
        on_touch_start: rx.EventHandler[touch_handler]
        on_touch_start_capture: rx.EventHandler[touch_handler]

        # Pointer Events
        on_pointer_down: rx.EventHandler[pointer_handler]
        on_pointer_down_capture: rx.EventHandler[pointer_handler]
        on_pointer_move: rx.EventHandler[pointer_handler]
        on_pointer_move_capture: rx.EventHandler[pointer_handler]
        on_pointer_up: rx.EventHandler[pointer_handler]
        on_pointer_up_capture: rx.EventHandler[pointer_handler]
        on_pointer_cancel: rx.EventHandler[pointer_handler]
        on_pointer_cancel_capture: rx.EventHandler[pointer_handler]
        on_pointer_enter: rx.EventHandler[pointer_handler]  # Uses PointerEvent
        on_pointer_leave: rx.EventHandler[pointer_handler]  # Uses PointerEvent
        on_pointer_over: rx.EventHandler[pointer_handler]
        on_pointer_over_capture: rx.EventHandler[pointer_handler]
        on_pointer_out: rx.EventHandler[pointer_handler]
        on_pointer_out_capture: rx.EventHandler[pointer_handler]
        on_got_pointer_capture: rx.EventHandler[pointer_handler]
        on_got_pointer_capture_capture: rx.EventHandler[pointer_handler]
        on_lost_pointer_capture: rx.EventHandler[pointer_handler]
        on_lost_pointer_capture_capture: rx.EventHandler[pointer_handler]

        # UI Events (Usually UIEvent or SyntheticEvent)
        on_scroll: rx.EventHandler[ui_handler]
        on_scroll_capture: rx.EventHandler[ui_handler]
        on_scroll_end: rx.EventHandler[ui_handler]  # Assuming UIEvent
        on_scroll_end_capture: rx.EventHandler[ui_handler]

        # Wheel Events
        on_wheel: rx.EventHandler[wheel_handler]
        on_wheel_capture: rx.EventHandler[wheel_handler]

        # Animation Events
        on_animation_start: rx.EventHandler[animation_handler]
        on_animation_start_capture: rx.EventHandler[animation_handler]
        on_animation_end: rx.EventHandler[animation_handler]
        on_animation_end_capture: rx.EventHandler[animation_handler]
        on_animation_iteration: rx.EventHandler[animation_handler]
        on_animation_iteration_capture: rx.EventHandler[animation_handler]

        # Toggle Events
        on_toggle: rx.EventHandler[toggle_handler]
        on_before_toggle: rx.EventHandler[toggle_handler]  # Assuming ToggleEvent

        # Transition Events
        on_transition_cancel: rx.EventHandler[transition_handler]
        on_transition_cancel_capture: rx.EventHandler[transition_handler]
        on_transition_end: rx.EventHandler[transition_handler]
        on_transition_end_capture: rx.EventHandler[transition_handler]
        on_transition_run: rx.EventHandler[transition_handler]
        on_transition_run_capture: rx.EventHandler[transition_handler]
        on_transition_start: rx.EventHandler[transition_handler]
        on_transition_start_capture: rx.EventHandler[transition_handler]

    return DOMEventsMixin
