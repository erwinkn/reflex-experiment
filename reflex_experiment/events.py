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
)
import reflex as rx
from pydantic.v1 import BaseModel
from pydantic.v1.generics import GenericModel

# Import base element type and specific elements if needed for defaults or bounds
from .elements import (
    HTMLElementField,
    HTMLElement,
    HTMLElementBase,  # Import the Union type
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
    target: HTMLElement = HTMLElementField  # target of the event (may be a child)
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
    target: TElement = HTMLElementField
    related_target: Optional[HTMLElementBase] = (
        HTMLElementField  # (EventTarget & RelatedTarget) | null
    )


class FormEvent(SyntheticEvent, Generic[TElement]):
    # No specific fields added here
    pass


class InvalidEvent(SyntheticEvent, Generic[TElement]):
    target: TElement = HTMLElementField


class ChangeEvent(SyntheticEvent, Generic[TElement]):
    target: TElement = HTMLElementField


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


def event_handler(var):
    # TODO
    return [var]


class DOMEventsMixin(rx.Component):
    # Clipboard Events
    on_copy: rx.EventHandler[event_handler]
    on_copy_capture: rx.EventHandler[event_handler]
    on_cut: rx.EventHandler[event_handler]
    on_cut_capture: rx.EventHandler[event_handler]
    on_paste: rx.EventHandler[event_handler]
    on_paste_capture: rx.EventHandler[event_handler]

    # Composition Events
    on_composition_end: rx.EventHandler[event_handler]
    on_composition_end_capture: rx.EventHandler[event_handler]
    on_composition_start: rx.EventHandler[event_handler]
    on_composition_start_capture: rx.EventHandler[event_handler]
    on_composition_update: rx.EventHandler[event_handler]
    on_composition_update_capture: rx.EventHandler[event_handler]

    # Focus Events
    on_focus: rx.EventHandler[event_handler]
    on_focus_capture: rx.EventHandler[event_handler]
    on_blur: rx.EventHandler[event_handler]
    on_blur_capture: rx.EventHandler[event_handler]

    # Form Events
    # Use the specific change event handlers if desired, otherwise use the generic one.
    # Using generic 'change_event' for broader compatibility.
    on_change: rx.EventHandler[event_handler]
    on_change_capture: rx.EventHandler[event_handler]
    # on_change: rx.EventHandler[event_handler] # Example for input-specific
    on_before_input: rx.EventHandler[event_handler]  # FormEvent is often used
    on_before_input_capture: rx.EventHandler[event_handler]
    on_input: rx.EventHandler[event_handler]  # FormEvent is often used
    on_input_capture: rx.EventHandler[event_handler]
    on_reset: rx.EventHandler[event_handler]
    on_reset_capture: rx.EventHandler[event_handler]
    on_submit: rx.EventHandler[event_handler]
    on_submit_capture: rx.EventHandler[event_handler]
    on_invalid: rx.EventHandler[event_handler]
    on_invalid_capture: rx.EventHandler[event_handler]

    # Image Events (Usually SyntheticEvent)
    on_load: rx.EventHandler[event_handler]
    on_load_capture: rx.EventHandler[event_handler]
    on_error: rx.EventHandler[event_handler]  # also a Media Event
    on_error_capture: rx.EventHandler[event_handler]  # also a Media Event

    # Keyboard Events
    on_key_down: rx.EventHandler[event_handler]
    on_key_down_capture: rx.EventHandler[event_handler]
    # on_key_press: rx.EventHandler[event_handler] # deprecated
    # on_key_press_capture: rx.EventHandler[event_handler] # deprecated
    on_key_up: rx.EventHandler[event_handler]
    on_key_up_capture: rx.EventHandler[event_handler]

    # Media Events (Usually SyntheticEvent)
    on_abort: rx.EventHandler[event_handler]
    on_abort_capture: rx.EventHandler[event_handler]
    on_can_play: rx.EventHandler[event_handler]
    on_can_play_capture: rx.EventHandler[event_handler]
    on_can_play_through: rx.EventHandler[event_handler]
    on_can_play_through_capture: rx.EventHandler[event_handler]
    on_duration_change: rx.EventHandler[event_handler]
    on_duration_change_capture: rx.EventHandler[event_handler]
    on_emptied: rx.EventHandler[event_handler]
    on_emptied_capture: rx.EventHandler[event_handler]
    on_encrypted: rx.EventHandler[event_handler]
    on_encrypted_capture: rx.EventHandler[event_handler]
    on_ended: rx.EventHandler[event_handler]
    on_ended_capture: rx.EventHandler[event_handler]
    on_loaded_data: rx.EventHandler[event_handler]
    on_loaded_data_capture: rx.EventHandler[event_handler]
    on_loaded_metadata: rx.EventHandler[event_handler]
    on_loaded_metadata_capture: rx.EventHandler[event_handler]
    on_load_start: rx.EventHandler[event_handler]
    on_load_start_capture: rx.EventHandler[event_handler]
    on_pause: rx.EventHandler[event_handler]
    on_pause_capture: rx.EventHandler[event_handler]
    on_play: rx.EventHandler[event_handler]
    on_play_capture: rx.EventHandler[event_handler]
    on_playing: rx.EventHandler[event_handler]
    on_playing_capture: rx.EventHandler[event_handler]
    on_progress: rx.EventHandler[event_handler]
    on_progress_capture: rx.EventHandler[event_handler]
    on_rate_change: rx.EventHandler[event_handler]
    on_rate_change_capture: rx.EventHandler[event_handler]
    on_resize: rx.EventHandler[event_handler]
    on_resize_capture: rx.EventHandler[event_handler]
    on_seeked: rx.EventHandler[event_handler]
    on_seeked_capture: rx.EventHandler[event_handler]
    on_seeking: rx.EventHandler[event_handler]
    on_seeking_capture: rx.EventHandler[event_handler]
    on_stalled: rx.EventHandler[event_handler]
    on_stalled_capture: rx.EventHandler[event_handler]
    on_suspend: rx.EventHandler[event_handler]
    on_suspend_capture: rx.EventHandler[event_handler]
    on_time_update: rx.EventHandler[event_handler]
    on_time_update_capture: rx.EventHandler[event_handler]
    on_volume_change: rx.EventHandler[event_handler]
    on_volume_change_capture: rx.EventHandler[event_handler]
    on_waiting: rx.EventHandler[event_handler]
    on_waiting_capture: rx.EventHandler[event_handler]

    # Mouse Events (Using pointer_event for consistency where applicable, mouse_event otherwise)
    on_aux_click: rx.EventHandler[event_handler]
    on_aux_click_capture: rx.EventHandler[event_handler]
    on_click: rx.EventHandler[event_handler]  # Often PointerEvent in modern React
    on_click_capture: rx.EventHandler[event_handler]
    on_context_menu: rx.EventHandler[event_handler]
    on_context_menu_capture: rx.EventHandler[event_handler]
    on_double_click: rx.EventHandler[event_handler]
    on_double_click_capture: rx.EventHandler[event_handler]
    on_drag: rx.EventHandler[event_handler]
    on_drag_capture: rx.EventHandler[event_handler]
    on_drag_end: rx.EventHandler[event_handler]
    on_drag_end_capture: rx.EventHandler[event_handler]
    on_drag_enter: rx.EventHandler[event_handler]
    on_drag_enter_capture: rx.EventHandler[event_handler]
    on_drag_exit: rx.EventHandler[event_handler]
    on_drag_exit_capture: rx.EventHandler[event_handler]
    on_drag_leave: rx.EventHandler[event_handler]
    on_drag_leave_capture: rx.EventHandler[event_handler]
    on_drag_over: rx.EventHandler[event_handler]
    on_drag_over_capture: rx.EventHandler[event_handler]
    on_drag_start: rx.EventHandler[event_handler]
    on_drag_start_capture: rx.EventHandler[event_handler]
    on_drop: rx.EventHandler[event_handler]
    on_drop_capture: rx.EventHandler[event_handler]
    on_mouse_down: rx.EventHandler[event_handler]
    on_mouse_down_capture: rx.EventHandler[event_handler]
    on_mouse_enter: rx.EventHandler[event_handler]  # Uses MouseEvent
    on_mouse_leave: rx.EventHandler[event_handler]  # Uses MouseEvent
    on_mouse_move: rx.EventHandler[event_handler]
    on_mouse_move_capture: rx.EventHandler[event_handler]
    on_mouse_out: rx.EventHandler[event_handler]
    on_mouse_out_capture: rx.EventHandler[event_handler]
    on_mouse_over: rx.EventHandler[event_handler]
    on_mouse_over_capture: rx.EventHandler[event_handler]
    on_mouse_up: rx.EventHandler[event_handler]
    on_mouse_up_capture: rx.EventHandler[event_handler]

    # Selection Events (Usually SyntheticEvent)
    on_select: rx.EventHandler[event_handler]
    on_select_capture: rx.EventHandler[event_handler]

    # Touch Events
    on_touch_cancel: rx.EventHandler[event_handler]
    on_touch_cancel_capture: rx.EventHandler[event_handler]
    on_touch_end: rx.EventHandler[event_handler]
    on_touch_end_capture: rx.EventHandler[event_handler]
    on_touch_move: rx.EventHandler[event_handler]
    on_touch_move_capture: rx.EventHandler[event_handler]
    on_touch_start: rx.EventHandler[event_handler]
    on_touch_start_capture: rx.EventHandler[event_handler]

    # Pointer Events
    on_pointer_down: rx.EventHandler[event_handler]
    on_pointer_down_capture: rx.EventHandler[event_handler]
    on_pointer_move: rx.EventHandler[event_handler]
    on_pointer_move_capture: rx.EventHandler[event_handler]
    on_pointer_up: rx.EventHandler[event_handler]
    on_pointer_up_capture: rx.EventHandler[event_handler]
    on_pointer_cancel: rx.EventHandler[event_handler]
    on_pointer_cancel_capture: rx.EventHandler[event_handler]
    on_pointer_enter: rx.EventHandler[event_handler]  # Uses PointerEvent
    on_pointer_leave: rx.EventHandler[event_handler]  # Uses PointerEvent
    on_pointer_over: rx.EventHandler[event_handler]
    on_pointer_over_capture: rx.EventHandler[event_handler]
    on_pointer_out: rx.EventHandler[event_handler]
    on_pointer_out_capture: rx.EventHandler[event_handler]
    on_got_pointer_capture: rx.EventHandler[event_handler]
    on_got_pointer_capture_capture: rx.EventHandler[event_handler]
    on_lost_pointer_capture: rx.EventHandler[event_handler]
    on_lost_pointer_capture_capture: rx.EventHandler[event_handler]

    # UI Events (Usually UIEvent or SyntheticEvent)
    on_scroll: rx.EventHandler[event_handler]
    on_scroll_capture: rx.EventHandler[event_handler]
    on_scroll_end: rx.EventHandler[event_handler]  # Assuming UIEvent
    on_scroll_end_capture: rx.EventHandler[event_handler]

    # Wheel Events
    on_wheel: rx.EventHandler[event_handler]
    on_wheel_capture: rx.EventHandler[event_handler]

    # Animation Events
    on_animation_start: rx.EventHandler[event_handler]
    on_animation_start_capture: rx.EventHandler[event_handler]
    on_animation_end: rx.EventHandler[event_handler]
    on_animation_end_capture: rx.EventHandler[event_handler]
    on_animation_iteration: rx.EventHandler[event_handler]
    on_animation_iteration_capture: rx.EventHandler[event_handler]

    # Toggle Events
    on_toggle: rx.EventHandler[event_handler]
    on_before_toggle: rx.EventHandler[event_handler]  # Assuming ToggleEvent

    # Transition Events
    on_transition_cancel: rx.EventHandler[event_handler]
    on_transition_cancel_capture: rx.EventHandler[event_handler]
    on_transition_end: rx.EventHandler[event_handler]
    on_transition_end_capture: rx.EventHandler[event_handler]
    on_transition_run: rx.EventHandler[event_handler]
    on_transition_run_capture: rx.EventHandler[event_handler]
    on_transition_start: rx.EventHandler[event_handler]
    on_transition_start_capture: rx.EventHandler[event_handler]


class DOMEvents(TypedDict):
    # Clipboard Events
    on_copy: rx.EventHandler[clipboard_event]
    on_copy_capture: rx.EventHandler[clipboard_event]
    on_cut: rx.EventHandler[clipboard_event]
    on_cut_capture: rx.EventHandler[clipboard_event]
    on_paste: rx.EventHandler[clipboard_event]
    on_paste_capture: rx.EventHandler[clipboard_event]

    # Composition Events
    on_composition_end: rx.EventHandler[composition_event]
    on_composition_end_capture: rx.EventHandler[composition_event]
    on_composition_start: rx.EventHandler[composition_event]
    on_composition_start_capture: rx.EventHandler[composition_event]
    on_composition_update: rx.EventHandler[composition_event]
    on_composition_update_capture: rx.EventHandler[composition_event]

    # Focus Events
    on_focus: rx.EventHandler[focus_event]
    on_focus_capture: rx.EventHandler[focus_event]
    on_blur: rx.EventHandler[focus_event]
    on_blur_capture: rx.EventHandler[focus_event]

    # Form Events
    # Use the specific change event handlers if desired, otherwise use the generic one.
    # Using generic 'change_event' for broader compatibility.
    on_change: rx.EventHandler[change_event]
    on_change_capture: rx.EventHandler[change_event]
    # on_change: rx.EventHandler[input_change_event] # Example for input-specific
    on_before_input: rx.EventHandler[form_event]  # FormEvent is often used
    on_before_input_capture: rx.EventHandler[form_event]
    on_input: rx.EventHandler[form_event]  # FormEvent is often used
    on_input_capture: rx.EventHandler[form_event]
    on_reset: rx.EventHandler[form_event]
    on_reset_capture: rx.EventHandler[form_event]
    on_submit: rx.EventHandler[form_event]
    on_submit_capture: rx.EventHandler[form_event]
    on_invalid: rx.EventHandler[invalid_event]
    on_invalid_capture: rx.EventHandler[invalid_event]

    # Image Events (Usually SyntheticEvent)
    on_load: rx.EventHandler[synthetic_event]
    on_load_capture: rx.EventHandler[synthetic_event]
    on_error: rx.EventHandler[synthetic_event]  # also a Media Event
    on_error_capture: rx.EventHandler[synthetic_event]  # also a Media Event

    # Keyboard Events
    on_key_down: rx.EventHandler[keyboard_event]
    on_key_down_capture: rx.EventHandler[keyboard_event]
    # on_key_press: rx.EventHandler[keyboard_event] # deprecated
    # on_key_press_capture: rx.EventHandler[keyboard_event] # deprecated
    on_key_up: rx.EventHandler[keyboard_event]
    on_key_up_capture: rx.EventHandler[keyboard_event]

    # Media Events (Usually SyntheticEvent)
    on_abort: rx.EventHandler[synthetic_event]
    on_abort_capture: rx.EventHandler[synthetic_event]
    on_can_play: rx.EventHandler[synthetic_event]
    on_can_play_capture: rx.EventHandler[synthetic_event]
    on_can_play_through: rx.EventHandler[synthetic_event]
    on_can_play_through_capture: rx.EventHandler[synthetic_event]
    on_duration_change: rx.EventHandler[synthetic_event]
    on_duration_change_capture: rx.EventHandler[synthetic_event]
    on_emptied: rx.EventHandler[synthetic_event]
    on_emptied_capture: rx.EventHandler[synthetic_event]
    on_encrypted: rx.EventHandler[synthetic_event]
    on_encrypted_capture: rx.EventHandler[synthetic_event]
    on_ended: rx.EventHandler[synthetic_event]
    on_ended_capture: rx.EventHandler[synthetic_event]
    on_loaded_data: rx.EventHandler[synthetic_event]
    on_loaded_data_capture: rx.EventHandler[synthetic_event]
    on_loaded_metadata: rx.EventHandler[synthetic_event]
    on_loaded_metadata_capture: rx.EventHandler[synthetic_event]
    on_load_start: rx.EventHandler[synthetic_event]
    on_load_start_capture: rx.EventHandler[synthetic_event]
    on_pause: rx.EventHandler[synthetic_event]
    on_pause_capture: rx.EventHandler[synthetic_event]
    on_play: rx.EventHandler[synthetic_event]
    on_play_capture: rx.EventHandler[synthetic_event]
    on_playing: rx.EventHandler[synthetic_event]
    on_playing_capture: rx.EventHandler[synthetic_event]
    on_progress: rx.EventHandler[synthetic_event]
    on_progress_capture: rx.EventHandler[synthetic_event]
    on_rate_change: rx.EventHandler[synthetic_event]
    on_rate_change_capture: rx.EventHandler[synthetic_event]
    on_resize: rx.EventHandler[synthetic_event]
    on_resize_capture: rx.EventHandler[synthetic_event]
    on_seeked: rx.EventHandler[synthetic_event]
    on_seeked_capture: rx.EventHandler[synthetic_event]
    on_seeking: rx.EventHandler[synthetic_event]
    on_seeking_capture: rx.EventHandler[synthetic_event]
    on_stalled: rx.EventHandler[synthetic_event]
    on_stalled_capture: rx.EventHandler[synthetic_event]
    on_suspend: rx.EventHandler[synthetic_event]
    on_suspend_capture: rx.EventHandler[synthetic_event]
    on_time_update: rx.EventHandler[synthetic_event]
    on_time_update_capture: rx.EventHandler[synthetic_event]
    on_volume_change: rx.EventHandler[synthetic_event]
    on_volume_change_capture: rx.EventHandler[synthetic_event]
    on_waiting: rx.EventHandler[synthetic_event]
    on_waiting_capture: rx.EventHandler[synthetic_event]

    # Mouse Events (Using pointer_event for consistency where applicable, mouse_event otherwise)
    on_aux_click: rx.EventHandler[mouse_event]
    on_aux_click_capture: rx.EventHandler[mouse_event]
    on_click: rx.EventHandler[pointer_event]  # Often PointerEvent in modern React
    on_click_capture: rx.EventHandler[pointer_event]
    on_context_menu: rx.EventHandler[mouse_event]
    on_context_menu_capture: rx.EventHandler[mouse_event]
    on_double_click: rx.EventHandler[mouse_event]
    on_double_click_capture: rx.EventHandler[mouse_event]
    on_drag: rx.EventHandler[drag_event]
    on_drag_capture: rx.EventHandler[drag_event]
    on_drag_end: rx.EventHandler[drag_event]
    on_drag_end_capture: rx.EventHandler[drag_event]
    on_drag_enter: rx.EventHandler[drag_event]
    on_drag_enter_capture: rx.EventHandler[drag_event]
    on_drag_exit: rx.EventHandler[drag_event]
    on_drag_exit_capture: rx.EventHandler[drag_event]
    on_drag_leave: rx.EventHandler[drag_event]
    on_drag_leave_capture: rx.EventHandler[drag_event]
    on_drag_over: rx.EventHandler[drag_event]
    on_drag_over_capture: rx.EventHandler[drag_event]
    on_drag_start: rx.EventHandler[drag_event]
    on_drag_start_capture: rx.EventHandler[drag_event]
    on_drop: rx.EventHandler[drag_event]
    on_drop_capture: rx.EventHandler[drag_event]
    on_mouse_down: rx.EventHandler[mouse_event]
    on_mouse_down_capture: rx.EventHandler[mouse_event]
    on_mouse_enter: rx.EventHandler[mouse_event]  # Uses MouseEvent
    on_mouse_leave: rx.EventHandler[mouse_event]  # Uses MouseEvent
    on_mouse_move: rx.EventHandler[mouse_event]
    on_mouse_move_capture: rx.EventHandler[mouse_event]
    on_mouse_out: rx.EventHandler[mouse_event]
    on_mouse_out_capture: rx.EventHandler[mouse_event]
    on_mouse_over: rx.EventHandler[mouse_event]
    on_mouse_over_capture: rx.EventHandler[mouse_event]
    on_mouse_up: rx.EventHandler[mouse_event]
    on_mouse_up_capture: rx.EventHandler[mouse_event]

    # Selection Events (Usually SyntheticEvent)
    on_select: rx.EventHandler[synthetic_event]
    on_select_capture: rx.EventHandler[synthetic_event]

    # Touch Events
    on_touch_cancel: rx.EventHandler[touch_event]
    on_touch_cancel_capture: rx.EventHandler[touch_event]
    on_touch_end: rx.EventHandler[touch_event]
    on_touch_end_capture: rx.EventHandler[touch_event]
    on_touch_move: rx.EventHandler[touch_event]
    on_touch_move_capture: rx.EventHandler[touch_event]
    on_touch_start: rx.EventHandler[touch_event]
    on_touch_start_capture: rx.EventHandler[touch_event]

    # Pointer Events
    on_pointer_down: rx.EventHandler[pointer_event]
    on_pointer_down_capture: rx.EventHandler[pointer_event]
    on_pointer_move: rx.EventHandler[pointer_event]
    on_pointer_move_capture: rx.EventHandler[pointer_event]
    on_pointer_up: rx.EventHandler[pointer_event]
    on_pointer_up_capture: rx.EventHandler[pointer_event]
    on_pointer_cancel: rx.EventHandler[pointer_event]
    on_pointer_cancel_capture: rx.EventHandler[pointer_event]
    on_pointer_enter: rx.EventHandler[pointer_event]  # Uses PointerEvent
    on_pointer_leave: rx.EventHandler[pointer_event]  # Uses PointerEvent
    on_pointer_over: rx.EventHandler[pointer_event]
    on_pointer_over_capture: rx.EventHandler[pointer_event]
    on_pointer_out: rx.EventHandler[pointer_event]
    on_pointer_out_capture: rx.EventHandler[pointer_event]
    on_got_pointer_capture: rx.EventHandler[pointer_event]
    on_got_pointer_capture_capture: rx.EventHandler[pointer_event]
    on_lost_pointer_capture: rx.EventHandler[pointer_event]
    on_lost_pointer_capture_capture: rx.EventHandler[pointer_event]

    # UI Events (Usually UIEvent or SyntheticEvent)
    on_scroll: rx.EventHandler[ui_event]
    on_scroll_capture: rx.EventHandler[ui_event]
    on_scroll_end: rx.EventHandler[ui_event]  # Assuming UIEvent
    on_scroll_end_capture: rx.EventHandler[ui_event]

    # Wheel Events
    on_wheel: rx.EventHandler[wheel_event]
    on_wheel_capture: rx.EventHandler[wheel_event]

    # Animation Events
    on_animation_start: rx.EventHandler[animation_event]
    on_animation_start_capture: rx.EventHandler[animation_event]
    on_animation_end: rx.EventHandler[animation_event]
    on_animation_end_capture: rx.EventHandler[animation_event]
    on_animation_iteration: rx.EventHandler[animation_event]
    on_animation_iteration_capture: rx.EventHandler[animation_event]

    # Toggle Events
    on_toggle: rx.EventHandler[toggle_event]
    on_before_toggle: rx.EventHandler[toggle_event]  # Assuming ToggleEvent

    # Transition Events
    on_transition_cancel: rx.EventHandler[transition_event]
    on_transition_cancel_capture: rx.EventHandler[transition_event]
    on_transition_end: rx.EventHandler[transition_event]
    on_transition_end_capture: rx.EventHandler[transition_event]
    on_transition_run: rx.EventHandler[transition_event]
    on_transition_run_capture: rx.EventHandler[transition_event]
    on_transition_start: rx.EventHandler[transition_event]
    on_transition_start_capture: rx.EventHandler[transition_event]
