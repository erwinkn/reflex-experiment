# Adapted from @types/react 19.0
# Notes:
# - We cannot serialize or use any methods on event objects or their targets
# - We can only serialize data
# - This makes the EventTarget type effectively empty

from dataclasses import dataclass
import dataclasses
from typing import (
    Any,
    Callable,
    Literal,
    TypedDict,
    Generic,
    TypeVar,
    Type,
    Optional,
    Union,
    List,
)
import reflex as rx
from reflex.base import Base
from reflex.vars import ObjectVar, Var

# Import base element type and specific elements if needed for defaults or bounds
from .elements import (
    BaseHTMLElement,
    Element,
    HTMLElementField,
    HTMLInputElement,
    HTMLSelectElement,
    HTMLTextAreaElement,
    HTMLElement,  # Import the Union type
)  # Example imports


# Generic TypeVar for the element target
TElement = TypeVar("TElement", bound=HTMLElement)
TRelatedTarget = TypeVar(
    "TRelatedTarget", bound=HTMLElement
)  # relatedTarget can be null


# Base data classes using rx.Base
class DataTransferItem(Base):
    kind: str
    type: str


class DataTransfer(Base):
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


class Touch(Base):
    target: HTMLElement = HTMLElementField
    identifier: int
    screen_x: float
    screen_y: float
    client_x: float
    client_y: float
    page_x: float
    page_y: float


# Base SyntheticEvent using rx.Base and Generic
class SyntheticEvent(Base, Generic[TElement]):
    # nativeEvent: Any # Omitted
    current_target: TElement  # element on which the event listener is registered
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
    time_stamp: int
    type: str


class UIEvent(SyntheticEvent[TElement], Generic[TElement]):
    detail: int
    # view: Any # AbstractView - Omitted


class MouseEvent(UIEvent[TElement], Generic[TElement]):
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
    related_target: Optional[HTMLElement]
    screen_x: float
    screen_y: float
    shift_key: bool


class ClipboardEvent(SyntheticEvent[TElement], Generic[TElement]):
    clipboard_data: DataTransfer


class CompositionEvent(SyntheticEvent[TElement], Generic[TElement]):
    data: str


class DragEvent(MouseEvent[TElement], Generic[TElement]):
    data_transfer: DataTransfer


class PointerEvent(MouseEvent[TElement], Generic[TElement]):
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
    SyntheticEvent[TElement],
    Generic[TElement],
):
    target: TElement
    related_target: Optional[HTMLElement]  # (EventTarget & RelatedTarget) | null


class FormEvent(SyntheticEvent[TElement], Generic[TElement]):
    # No specific fields added here
    pass


class InvalidEvent(SyntheticEvent[TElement], Generic[TElement]):
    target: TElement


class ChangeEvent(SyntheticEvent[TElement], Generic[TElement]):
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


class KeyboardEvent(UIEvent[TElement], Generic[TElement]):
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


class TouchEvent(UIEvent[TElement], Generic[TElement]):
    alt_key: bool
    changed_touches: list[Touch]  # TouchList
    ctrl_key: bool
    # getModifierState(key: ModifierKey): boolean
    meta_key: bool
    shift_key: bool
    target_touches: list[Touch]  # TouchList
    touches: list[Touch]  # TouchList


class WheelEvent(MouseEvent[TElement], Generic[TElement]):
    delta_mode: int
    delta_x: float
    delta_y: float
    delta_z: float


class AnimationEvent(SyntheticEvent[TElement], Generic[TElement]):
    animation_name: str
    elapsed_time: float
    pseudo_element: str


class ToggleEvent(SyntheticEvent[TElement], Generic[TElement]):
    old_state: Literal["closed", "open"]
    new_state: Literal["closed", "open"]


class TransitionEvent(SyntheticEvent[TElement], Generic[TElement]):
    elapsed_time: float
    property_name: str
    pseudo_element: str


def create_event_handler(
    data_class: Type[Base],
    # element_type: Type[Element] = Element,
    # target_type: Type[Element] = Element,
    # related_target_type: Optional[
    #     Type[Element]
    # ] = Element,  # Default to Element for FocusEvent
):
    """Create an event handler function for a rx.Base model representing a React event."""

    # Define the inner handler function
    def event_handler(e: ObjectVar[Any]) -> tuple[Var[Base]]:
        field_dict = {}
        # Use get_fields() for rx.Base (Pydantic v1) models
        for name, field in data_class.get_fields().items():
            # Convert snake_case (Python model field name) to camelCase (JS event property name)
            camel_name = "".join(
                word.capitalize() if i > 0 else word
                for i, word in enumerate(name.split("_"))
            )
            # Handle specific name mappings
            if name == "type":
                camel_name = "type"
            elif name == "html_for":
                camel_name = "htmlFor"
            elif name == "class_name":
                camel_name = "className"
            elif name == "current_target":
                camel_name = "currentTarget"
            elif name == "related_target":
                camel_name = "relatedTarget"
            # Add other specific mappings if needed

            # Access the property on the JS event object Var using getattr
            try:
                js_value = getattr(e, camel_name)
            except AttributeError:
                # Handle cases where the attribute might not exist on the event
                # Depending on the field definition (Optional or not), assign None or raise error
                # For simplicity, let's assign a Var(None) if optional, otherwise error prone
                if field.allow_none:
                    js_value = Var.create(None)
                else:
                    # This case might indicate a mismatch or an unexpected event structure
                    print(
                        f"Warning: Attribute '{camel_name}' not found on event object for required field '{name}'."
                    )
                    # Assigning None might lead to validation errors later if not optional
                    js_value = Var.create(None)

            # Recursively handle nested Base models
            field_type = field.outer_type_
            is_optional = field.allow_none

            # Check if field_type is a rx.Base model (or Optional[rx.Base])
            # Correct way to check for Union with NoneType for Optional
            origin_type = getattr(field_type, "__origin__", None)
            type_args = getattr(field_type, "__args__", [])

            nested_base_type = None
            if origin_type is Union and type(None) in type_args:
                # It's Optional[Something]
                nested_base_type = next(
                    (
                        t
                        for t in type_args
                        if isinstance(t, type)
                        and issubclass(t, Base)
                        and t is not type(None)
                    ),
                    None,
                )
            elif isinstance(field_type, type) and issubclass(field_type, Base):
                nested_base_type = field_type

            # Also handle lists of Base models
            is_list_of_base = False
            list_item_type = None
            if origin_type is list and type_args:
                list_item_origin = getattr(type_args[0], "__origin__", None)
                list_item_args = getattr(type_args[0], "__args__", [])

                if isinstance(type_args[0], type) and issubclass(type_args[0], Base):
                    is_list_of_base = True
                    list_item_type = type_args[0]
                # Add checks for Optional[Base] inside list if needed

            if nested_base_type:
                # For nested single Base model
                # We assume js_value is already a Var representing the nested object
                # We just need to ensure the type is set correctly for potential validation/conversion
                # Pydantic v1 might require explicit dict conversion if js_value isn't structured right.
                # Let's assign js_value directly and set the type hint.
                field_dict[name] = js_value._replace(_var_type=nested_base_type)
            elif is_list_of_base and list_item_type:
                # For lists of Base models (like touches)
                # We assume js_value is a Var representing the JS array.
                # We need to map over it and ensure each item is typed.
                # This is complex with current Var operations. Let's assign the list Var directly
                # and type the whole list. Runtime conversion might be needed.
                # Typing the list Var: List[list_item_type]
                field_dict[name] = js_value._replace(_var_type=List[list_item_type])
            else:
                # Assign the direct JS value Var for primitive types or unhandled structures
                field_dict[name] = js_value

        # Create the final Var and explicitly type it to the original data_class
        # This assumes data_class itself might be generic, Pydantic should handle it.
        final_var = Var.create(field_dict)._replace(_var_type=data_class)
        return (final_var,)

    return event_handler


# Create specific event handlers
# For generic events, we might need to instantiate them with specific Element types
# if the defaults (Element, Element, Optional[Element]) are not sufficient.
# Example: For an input's onChange, target is often HTMLInputElement.
# handler = create_event_handler(ChangeEvent, target_type=HTMLInputElement)

# Define handlers with default Element types first
synthetic_event = create_event_handler(SyntheticEvent)
ui_event = create_event_handler(UIEvent)
mouse_event = create_event_handler(MouseEvent)
clipboard_event = create_event_handler(ClipboardEvent)
composition_event = create_event_handler(CompositionEvent)
drag_event = create_event_handler(DragEvent)
pointer_event = create_event_handler(PointerEvent)
focus_event = create_event_handler(FocusEvent)  # Uses default Element types
form_event = create_event_handler(FormEvent)
invalid_event = create_event_handler(InvalidEvent)
change_event = create_event_handler(ChangeEvent)
keyboard_event = create_event_handler(KeyboardEvent)
touch_event = create_event_handler(TouchEvent)
wheel_event = create_event_handler(WheelEvent)
animation_event = create_event_handler(AnimationEvent)
toggle_event = create_event_handler(ToggleEvent)
transition_event = create_event_handler(TransitionEvent)

# Special handler for ChangeEvent on specific input types (optional)
input_change_event = create_event_handler(ChangeEvent)
select_change_event = create_event_handler(ChangeEvent)
textarea_change_event = create_event_handler(ChangeEvent)


# Update DOMEvents to use rx.EventHandler with the created handlers
class DOMEvents(rx.Component):
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
