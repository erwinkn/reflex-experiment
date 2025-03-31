# Adapted from @types/react 19.0
# Notes:
# - We cannot serialize or use any methods on event objects or their targets
# - We can only serialize data
# - This makes the EventTarget type effectively empty

from dataclasses import dataclass
import dataclasses
from typing import Any, Callable, Literal, TypedDict, Generic, TypeVar, Type
import reflex as rx
from reflex.vars import ObjectVar, Var

# Import base element type and specific elements if needed for defaults or bounds
from .elements import (
    Element,
    HTMLInputElement,
    HTMLSelectElement,
    HTMLTextAreaElement,
)  # Example imports


# Generic TypeVar for the element target
TElement = TypeVar("TElement", bound=Element)
TTarget = TypeVar("TTarget", bound=Element)
TTarget2 = TypeVar("TTarget2", bound=Element)


# Base data classes remain the same
@dataclass
class DataTransferItem:
    kind: str
    type: str


@dataclass
class DataTransfer:
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
    files: Any  # FileList equivalent
    items: list[DataTransferItem]  # DataTransferItemList
    types: list[str]


@dataclass
class Touch(Generic[TTarget]):
    target: TTarget
    identifier: int
    screen_x: float
    screen_y: float
    client_x: float
    client_y: float
    page_x: float
    page_y: float


# Base SyntheticEvent is now Generic
@dataclass
class SyntheticEvent(Generic[TElement, TTarget]):
    # nativeEvent: Any 
    currentTarget: TElement # element on which the event listener is registered
    target: TTarget # target of the event (may be a child)
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
    time_stamp: int
    type: str


@dataclass
class UIEvent(SyntheticEvent):
    detail: int
    # view: Any # AbstractView


@dataclass
class MouseEvent(UIEvent):
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
    # related_target: Any  # EventTarget | null
    screen_x: float
    screen_y: float
    shift_key: bool


@dataclass
class ClipboardEvent(SyntheticEvent):
    clipboard_data: DataTransfer


@dataclass
class CompositionEvent(SyntheticEvent):
    data: str


@dataclass
class DragEvent(MouseEvent):
    data_transfer: DataTransfer


@dataclass
class PointerEvent(MouseEvent):
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


@dataclass
class FocusEvent(SyntheticEvent[TElement, TTarget], Generic[TElement,TTarget, TTarget2]):
    related_target: TTarget2  # (EventTarget & RelatedTarget) | null
    # target: TTarget


@dataclass
class FormEvent(SyntheticEvent):
    # target: TTarget  # EventTarget & T
    pass


@dataclass
class InvalidEvent(SyntheticEvent):
    # target: TTarget  # EventTarget & T
    pass


@dataclass
class ChangeEvent(SyntheticEvent):
    # target: TTarget  # EventTarget & T
    pass


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


@dataclass
class KeyboardEvent(UIEvent):
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


@dataclass
class TouchEvent(UIEvent):
    alt_key: bool
    changed_touches: list[Touch]  # TouchList
    ctrl_key: bool
    # getModifierState(key: ModifierKey): boolean
    meta_key: bool
    shift_key: bool
    target_touches: list[Touch]  # TouchList
    touches: list[Touch]  # TouchList


@dataclass
class WheelEvent(MouseEvent):
    delta_mode: int
    delta_x: float
    delta_y: float
    delta_z: float


@dataclass
class AnimationEvent(SyntheticEvent):
    animation_name: str
    elapsed_time: float
    pseudo_element: str


@dataclass
class ToggleEvent(SyntheticEvent):
    old_state: Literal["closed", "open"]
    new_state: Literal["closed", "open"]


@dataclass
class TransitionEvent(SyntheticEvent):
    elapsed_time: float
    property_name: str
    pseudo_element: str


def create_event_class(data_class: type) -> type:
    """Create an Event class from an EventData class definition."""
    fields_dict = {}
    for field in dataclasses.fields(data_class):
        # Convert snake_case to camelCase
        camel_name = "".join(
            word.capitalize() if i > 0 else word
            for i, word in enumerate(field.name.split("_"))
        )
        # Recursively create event class for nested dataclasses
        field_type = field.type
        if dataclasses.is_dataclass(field_type):
            field_type = create_event_class(field_type)
        fields_dict[camel_name] = field_type

    return dataclasses.make_dataclass(
        data_class.__name__.replace("Data", ""),
        fields_dict.items(),
    )


def create_event_handler(data_class: type):
    """Create an event handler function for a Data class."""
    event_class = create_event_class(data_class)

    def event_handler(e: ObjectVar[event_class]) -> tuple[Var[data_class]]:
        field_dict = {}
        for field in dataclasses.fields(data_class):
            camel_name = "".join(
                word.capitalize() if i > 0 else word
                for i, word in enumerate(field.name.split("_"))
            )
            value = getattr(e, camel_name)

            # Recursively handle nested dataclass fields
            if dataclasses.is_dataclass(field.type):
                nested_dict = {}
                for nested_field in dataclasses.fields(field.type):
                    nested_camel = "".join(
                        word.capitalize() if i > 0 else word
                        for i, word in enumerate(nested_field.name.split("_"))
                    )
                    nested_dict[nested_field.name] = getattr(value, nested_camel)
                field_dict[field.name] = Var.create(nested_dict).to(field.type)
            else:
                field_dict[field.name] = value

        return (Var.create(field_dict).to(data_class),)

    return event_handler


pointer_event = create_event_handler(PointerEvent)


class DOMEvents(rx.Component):
    on_copy: Callable[[dict], None]
    on_copy_capture: Callable[[dict], None]
    on_cut: Callable[[dict], None]
    on_cut_capture: Callable[[dict], None]
    on_paste: Callable[[dict], None]
    on_paste_capture: Callable[[dict], None]

    # Composition Events
    on_composition_end: Callable[[dict], None]
    on_composition_end_capture: Callable[[dict], None]
    on_composition_start: Callable[[dict], None]
    on_composition_start_capture: Callable[[dict], None]
    on_composition_update: Callable[[dict], None]
    on_composition_update_capture: Callable[[dict], None]

    # Focus Events
    on_focus: Callable[[dict], None]
    on_focus_capture: Callable[[dict], None]
    on_blur: Callable[[dict], None]
    on_blur_capture: Callable[[dict], None]

    # Form Events
    on_change: Callable[[dict], None]
    on_change_capture: Callable[[dict], None]
    on_before_input: Callable[[dict], None]
    on_before_input_capture: Callable[[dict], None]
    on_input: Callable[[dict], None]
    on_input_capture: Callable[[dict], None]
    on_reset: Callable[[dict], None]
    on_reset_capture: Callable[[dict], None]
    on_submit: Callable[[dict], None]
    on_submit_capture: Callable[[dict], None]
    on_invalid: Callable[[dict], None]
    on_invalid_capture: Callable[[dict], None]

    # Image Events
    on_load: Callable[[dict], None]
    on_load_capture: Callable[[dict], None]
    on_error: Callable[[dict], None]  # also a Media Event
    on_error_capture: Callable[[dict], None]  # also a Media Event

    # Keyboard Events
    on_key_down: Callable[[dict], None]
    on_key_down_capture: Callable[[dict], None]
    on_key_press: Callable[[dict], None]  # deprecated
    on_key_press_capture: Callable[[dict], None]  # deprecated
    on_key_up: Callable[[dict], None]
    on_key_up_capture: Callable[[dict], None]

    # Media Events
    on_abort: Callable[[dict], None]
    on_abort_capture: Callable[[dict], None]
    on_can_play: Callable[[dict], None]
    on_can_play_capture: Callable[[dict], None]
    on_can_play_through: Callable[[dict], None]
    on_can_play_through_capture: Callable[[dict], None]
    on_duration_change: Callable[[dict], None]
    on_duration_change_capture: Callable[[dict], None]
    on_emptied: Callable[[dict], None]
    on_emptied_capture: Callable[[dict], None]
    on_encrypted: Callable[[dict], None]
    on_encrypted_capture: Callable[[dict], None]
    on_ended: Callable[[dict], None]
    on_ended_capture: Callable[[dict], None]
    on_loaded_data: Callable[[dict], None]
    on_loaded_data_capture: Callable[[dict], None]
    on_loaded_metadata: Callable[[dict], None]
    on_loaded_metadata_capture: Callable[[dict], None]
    on_load_start: Callable[[dict], None]
    on_load_start_capture: Callable[[dict], None]
    on_pause: Callable[[dict], None]
    on_pause_capture: Callable[[dict], None]
    on_play: Callable[[dict], None]
    on_play_capture: Callable[[dict], None]
    on_playing: Callable[[dict], None]
    on_playing_capture: Callable[[dict], None]
    on_progress: Callable[[dict], None]
    on_progress_capture: Callable[[dict], None]
    on_rate_change: Callable[[dict], None]
    on_rate_change_capture: Callable[[dict], None]
    on_resize: Callable[[dict], None]
    on_resize_capture: Callable[[dict], None]
    on_seeked: Callable[[dict], None]
    on_seeked_capture: Callable[[dict], None]
    on_seeking: Callable[[dict], None]
    on_seeking_capture: Callable[[dict], None]
    on_stalled: Callable[[dict], None]
    on_stalled_capture: Callable[[dict], None]
    on_suspend: Callable[[dict], None]
    on_suspend_capture: Callable[[dict], None]
    on_time_update: Callable[[dict], None]
    on_time_update_capture: Callable[[dict], None]
    on_volume_change: Callable[[dict], None]
    on_volume_change_capture: Callable[[dict], None]
    on_waiting: Callable[[dict], None]
    on_waiting_capture: Callable[[dict], None]

    # Mouse Events
    on_aux_click: Callable[[dict], None]
    on_aux_click_capture: Callable[[dict], None]
    on_click: rx.EventHandler[pointer_event]
    on_click_capture: Callable[[dict], None]
    on_context_menu: Callable[[dict], None]
    on_context_menu_capture: Callable[[dict], None]
    on_double_click: Callable[[dict], None]
    on_double_click_capture: Callable[[dict], None]
    on_drag: Callable[[dict], None]
    on_drag_capture: Callable[[dict], None]
    on_drag_end: Callable[[dict], None]
    on_drag_end_capture: Callable[[dict], None]
    on_drag_enter: Callable[[dict], None]
    on_drag_enter_capture: Callable[[dict], None]
    on_drag_exit: Callable[[dict], None]
    on_drag_exit_capture: Callable[[dict], None]
    on_drag_leave: Callable[[dict], None]
    on_drag_leave_capture: Callable[[dict], None]
    on_drag_over: Callable[[dict], None]
    on_drag_over_capture: Callable[[dict], None]
    on_drag_start: Callable[[dict], None]
    on_drag_start_capture: Callable[[dict], None]
    on_drop: Callable[[dict], None]
    on_drop_capture: Callable[[dict], None]
    on_mouse_down: Callable[[dict], None]
    on_mouse_down_capture: Callable[[dict], None]
    on_mouse_enter: Callable[[dict], None]
    on_mouse_leave: Callable[[dict], None]
    on_mouse_move: Callable[[dict], None]
    on_mouse_move_capture: Callable[[dict], None]
    on_mouse_out: Callable[[dict], None]
    on_mouse_out_capture: Callable[[dict], None]
    on_mouse_over: Callable[[dict], None]
    on_mouse_over_capture: Callable[[dict], None]
    on_mouse_up: Callable[[dict], None]
    on_mouse_up_capture: Callable[[dict], None]

    # Selection Events
    on_select: Callable[[dict], None]
    on_select_capture: Callable[[dict], None]

    # Touch Events
    on_touch_cancel: Callable[[dict], None]
    on_touch_cancel_capture: Callable[[dict], None]
    on_touch_end: Callable[[dict], None]
    on_touch_end_capture: Callable[[dict], None]
    on_touch_move: Callable[[dict], None]
    on_touch_move_capture: Callable[[dict], None]
    on_touch_start: Callable[[dict], None]
    on_touch_start_capture: Callable[[dict], None]

    # Pointer Events
    on_pointer_down: rx.EventHandler[pointer_event]
    on_pointer_down_capture: rx.EventHandler[pointer_event]
    on_pointer_move: rx.EventHandler[pointer_event]
    on_pointer_move_capture: rx.EventHandler[pointer_event]
    on_pointer_up: rx.EventHandler[pointer_event]
    on_pointer_up_capture: rx.EventHandler[pointer_event]
    on_pointer_cancel: rx.EventHandler[pointer_event]
    on_pointer_cancel_capture: rx.EventHandler[pointer_event]
    on_pointer_enter: rx.EventHandler[pointer_event]
    on_pointer_leave: rx.EventHandler[pointer_event]
    on_pointer_over: rx.EventHandler[pointer_event]
    on_pointer_over_capture: rx.EventHandler[pointer_event]
    on_pointer_out: rx.EventHandler[pointer_event]
    on_pointer_out_capture: rx.EventHandler[pointer_event]
    on_got_pointer_capture: rx.EventHandler[pointer_event]
    on_got_pointer_capture_capture: rx.EventHandler[pointer_event]
    on_lost_pointer_capture: rx.EventHandler[pointer_event]
    on_lost_pointer_capture_capture: rx.EventHandler[pointer_event]

    # UI Events
    on_scroll: Callable[[dict], None]
    on_scroll_capture: Callable[[dict], None]
    on_scroll_end: Callable[[dict], None]
    on_scroll_end_capture: Callable[[dict], None]

    # Wheel Events
    on_wheel: Callable[[dict], None]
    on_wheel_capture: Callable[[dict], None]

    # Animation Events
    on_animation_start: Callable[[dict], None]
    on_animation_start_capture: Callable[[dict], None]
    on_animation_end: Callable[[dict], None]
    on_animation_end_capture: Callable[[dict], None]
    on_animation_iteration: Callable[[dict], None]
    on_animation_iteration_capture: Callable[[dict], None]

    # Toggle Events
    on_toggle: Callable[[dict], None]
    on_before_toggle: Callable[[dict], None]

    # Transition Events
    on_transition_cancel: Callable[[dict], None]
    on_transition_cancel_capture: Callable[[dict], None]
    on_transition_end: Callable[[dict], None]
    on_transition_end_capture: Callable[[dict], None]
    on_transition_run: Callable[[dict], None]
    on_transition_run_capture: Callable[[dict], None]
    on_transition_start: Callable[[dict], None]
    on_transition_start_capture: Callable[[dict], None]
