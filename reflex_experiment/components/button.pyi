"""Stub file for reflex_experiment/components/button.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import (
    Any,
    List,
    Literal,
    Optional,
    overload,
)
from reflex.event import EventType
from reflex.vars.base import Var
from reflex_experiment.events import (
    SyntheticEvent,
    UIEvent,
    ClipboardEvent,
    CompositionEvent,
    DragEvent,
    PointerEvent,
    FocusEvent,
    FormEvent,
    KeyboardEvent,
    MouseEvent,
    TouchEvent,
    WheelEvent,
    AnimationEvent,
    ToggleEvent,
    TransitionEvent,
)
from reflex_experiment.elements import (
    HTMLButtonElement,
)
from reflex_experiment.attributes import ButtonHTMLAttributes

class Button(ButtonHTMLAttributes):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        disabled: Var[bool] | bool | None = None,
        form: Var[str] | str | None = None,
        form_action: Var[str] | str | None = None,
        form_enc_type: Var[str] | str | None = None,
        form_method: Var[str] | str | None = None,
        form_no_validate: Var[bool] | bool | None = None,
        form_target: Var[str] | str | None = None,
        name: Var[str] | str | None = None,
        type: Literal["button", "reset", "submit"]
        | Var[Literal["button", "reset", "submit"]]
        | None = None,
        value: List[str] | Var[List[str] | int | str] | int | str | None = None,
        default_checked: Var[bool] | bool | None = None,
        default_value: List[str] | Var[List[str] | int | str] | int | str | None = None,
        suppress_content_editable_warning: Var[bool] | bool | None = None,
        suppress_hydration_warning: Var[bool] | bool | None = None,
        access_key: Var[str] | str | None = None,
        auto_capitalize: Literal[
            "characters", "none", "off", "on", "sentences", "words"
        ]
        | Var[Literal["characters", "none", "off", "on", "sentences", "words"]]
        | None = None,
        auto_focus: Var[bool] | bool | None = None,
        class_name: Var[str] | str | None = None,
        content_editable: Literal["false", "true", False, True]
        | Literal["inherit", "plaintext-only"]
        | Var[
            Literal["false", "true", False, True] | Literal["inherit", "plaintext-only"]
        ]
        | None = None,
        context_menu: Var[str] | str | None = None,
        dir: Var[str] | str | None = None,
        draggable: Literal["false", "true", False, True]
        | Var[Literal["false", "true", False, True]]
        | None = None,
        enter_key_hint: Literal[
            "done", "enter", "go", "next", "previous", "search", "send"
        ]
        | Var[Literal["done", "enter", "go", "next", "previous", "search", "send"]]
        | None = None,
        hidden: Var[bool] | bool | None = None,
        lang: Var[str] | str | None = None,
        nonce: Var[str] | str | None = None,
        slot: Var[str] | str | None = None,
        spell_check: Literal["false", "true", False, True]
        | Var[Literal["false", "true", False, True]]
        | None = None,
        tab_index: Var[int] | int | None = None,
        title: Var[str] | str | None = None,
        translate: Literal["no", "yes"] | Var[Literal["no", "yes"]] | None = None,
        radio_group: Var[str] | str | None = None,
        about: Var[str] | str | None = None,
        content: Var[str] | str | None = None,
        datatype: Var[str] | str | None = None,
        inlist: Any | Var[Any] | None = None,
        prefix: Var[str] | str | None = None,
        property: Var[str] | str | None = None,
        rel: Var[str] | str | None = None,
        resource: Var[str] | str | None = None,
        rev: Var[str] | str | None = None,
        typeof: Var[str] | str | None = None,
        vocab: Var[str] | str | None = None,
        auto_correct: Var[str] | str | None = None,
        auto_save: Var[str] | str | None = None,
        color: Var[str] | str | None = None,
        item_prop: Var[str] | str | None = None,
        item_scope: Var[bool] | bool | None = None,
        item_type: Var[str] | str | None = None,
        item_id: Var[str] | str | None = None,
        item_ref: Var[str] | str | None = None,
        results: Var[int] | int | None = None,
        security: Var[str] | str | None = None,
        unselectable: Literal["off", "on"] | Var[Literal["off", "on"]] | None = None,
        popover: Literal["", "auto", "manual"]
        | Var[Literal["", "auto", "manual"]]
        | None = None,
        popover_target_action: Literal["hide", "show", "toggle"]
        | Var[Literal["hide", "show", "toggle"]]
        | None = None,
        popover_target: Var[str] | str | None = None,
        inert: Var[bool] | bool | None = None,
        input_mode: Literal[
            "decimal", "email", "none", "numeric", "search", "tel", "text", "url"
        ]
        | Var[
            Literal[
                "decimal", "email", "none", "numeric", "search", "tel", "text", "url"
            ]
        ]
        | None = None,
        is_: Var[str] | str | None = None,
        exportparts: Var[str] | str | None = None,
        part: Var[str] | str | None = None,
        on_abort: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_abort_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_animation_end: Optional[
            EventType[()] | EventType[AnimationEvent[HTMLButtonElement]]
        ] = None,
        on_animation_end_capture: Optional[
            EventType[()] | EventType[AnimationEvent[HTMLButtonElement]]
        ] = None,
        on_animation_iteration: Optional[
            EventType[()] | EventType[AnimationEvent[HTMLButtonElement]]
        ] = None,
        on_animation_iteration_capture: Optional[
            EventType[()] | EventType[AnimationEvent[HTMLButtonElement]]
        ] = None,
        on_animation_start: Optional[
            EventType[()] | EventType[AnimationEvent[HTMLButtonElement]]
        ] = None,
        on_animation_start_capture: Optional[
            EventType[()] | EventType[AnimationEvent[HTMLButtonElement]]
        ] = None,
        on_aux_click: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_aux_click_capture: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_before_input: Optional[
            EventType[()] | EventType[FormEvent[HTMLButtonElement]]
        ] = None,
        on_before_input_capture: Optional[
            EventType[()] | EventType[FormEvent[HTMLButtonElement]]
        ] = None,
        on_before_toggle: Optional[
            EventType[()] | EventType[ToggleEvent[HTMLButtonElement]]
        ] = None,
        on_blur: Optional[
            EventType[()] | EventType[FocusEvent[HTMLButtonElement]]
        ] = None,
        on_blur_capture: Optional[
            EventType[()] | EventType[FocusEvent[HTMLButtonElement]]
        ] = None,
        on_can_play: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_can_play_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_can_play_through: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_can_play_through_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_change: Optional[
            EventType[()] | EventType[FocusEvent[HTMLButtonElement]]
        ] = None,
        on_change_capture: Optional[
            EventType[()] | EventType[FormEvent[HTMLButtonElement]]
        ] = None,
        on_click: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_click_capture: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_composition_end: Optional[
            EventType[()] | EventType[CompositionEvent[HTMLButtonElement]]
        ] = None,
        on_composition_end_capture: Optional[
            EventType[()] | EventType[CompositionEvent[HTMLButtonElement]]
        ] = None,
        on_composition_start: Optional[
            EventType[()] | EventType[CompositionEvent[HTMLButtonElement]]
        ] = None,
        on_composition_start_capture: Optional[
            EventType[()] | EventType[CompositionEvent[HTMLButtonElement]]
        ] = None,
        on_composition_update: Optional[
            EventType[()] | EventType[CompositionEvent[HTMLButtonElement]]
        ] = None,
        on_composition_update_capture: Optional[
            EventType[()] | EventType[CompositionEvent[HTMLButtonElement]]
        ] = None,
        on_context_menu: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_context_menu_capture: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_copy: Optional[
            EventType[()] | EventType[ClipboardEvent[HTMLButtonElement]]
        ] = None,
        on_copy_capture: Optional[
            EventType[()] | EventType[ClipboardEvent[HTMLButtonElement]]
        ] = None,
        on_cut: Optional[
            EventType[()] | EventType[ClipboardEvent[HTMLButtonElement]]
        ] = None,
        on_cut_capture: Optional[
            EventType[()] | EventType[ClipboardEvent[HTMLButtonElement]]
        ] = None,
        on_double_click: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_double_click_capture: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_drag: Optional[
            EventType[()] | EventType[DragEvent[HTMLButtonElement]]
        ] = None,
        on_drag_capture: Optional[
            EventType[()] | EventType[DragEvent[HTMLButtonElement]]
        ] = None,
        on_drag_end: Optional[
            EventType[()] | EventType[DragEvent[HTMLButtonElement]]
        ] = None,
        on_drag_end_capture: Optional[
            EventType[()] | EventType[DragEvent[HTMLButtonElement]]
        ] = None,
        on_drag_enter: Optional[
            EventType[()] | EventType[DragEvent[HTMLButtonElement]]
        ] = None,
        on_drag_enter_capture: Optional[
            EventType[()] | EventType[DragEvent[HTMLButtonElement]]
        ] = None,
        on_drag_exit: Optional[
            EventType[()] | EventType[DragEvent[HTMLButtonElement]]
        ] = None,
        on_drag_exit_capture: Optional[
            EventType[()] | EventType[DragEvent[HTMLButtonElement]]
        ] = None,
        on_drag_leave: Optional[
            EventType[()] | EventType[DragEvent[HTMLButtonElement]]
        ] = None,
        on_drag_leave_capture: Optional[
            EventType[()] | EventType[DragEvent[HTMLButtonElement]]
        ] = None,
        on_drag_over: Optional[
            EventType[()] | EventType[DragEvent[HTMLButtonElement]]
        ] = None,
        on_drag_over_capture: Optional[
            EventType[()] | EventType[DragEvent[HTMLButtonElement]]
        ] = None,
        on_drag_start: Optional[
            EventType[()] | EventType[DragEvent[HTMLButtonElement]]
        ] = None,
        on_drag_start_capture: Optional[
            EventType[()] | EventType[DragEvent[HTMLButtonElement]]
        ] = None,
        on_drop: Optional[
            EventType[()] | EventType[DragEvent[HTMLButtonElement]]
        ] = None,
        on_drop_capture: Optional[
            EventType[()] | EventType[DragEvent[HTMLButtonElement]]
        ] = None,
        on_duration_change: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_duration_change_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_emptied: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_emptied_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_encrypted: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_encrypted_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_ended: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_ended_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_error: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_error_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_focus: Optional[
            EventType[()] | EventType[FocusEvent[HTMLButtonElement]]
        ] = None,
        on_focus_capture: Optional[
            EventType[()] | EventType[FocusEvent[HTMLButtonElement]]
        ] = None,
        on_got_pointer_capture: Optional[
            EventType[()] | EventType[PointerEvent[HTMLButtonElement]]
        ] = None,
        on_got_pointer_capture_capture: Optional[
            EventType[()] | EventType[PointerEvent[HTMLButtonElement]]
        ] = None,
        on_input: Optional[
            EventType[()] | EventType[FormEvent[HTMLButtonElement]]
        ] = None,
        on_input_capture: Optional[
            EventType[()] | EventType[FormEvent[HTMLButtonElement]]
        ] = None,
        on_invalid: Optional[
            EventType[()] | EventType[FormEvent[HTMLButtonElement]]
        ] = None,
        on_invalid_capture: Optional[
            EventType[()] | EventType[FormEvent[HTMLButtonElement]]
        ] = None,
        on_key_down: Optional[
            EventType[()] | EventType[KeyboardEvent[HTMLButtonElement]]
        ] = None,
        on_key_down_capture: Optional[
            EventType[()] | EventType[KeyboardEvent[HTMLButtonElement]]
        ] = None,
        on_key_up: Optional[
            EventType[()] | EventType[KeyboardEvent[HTMLButtonElement]]
        ] = None,
        on_key_up_capture: Optional[
            EventType[()] | EventType[KeyboardEvent[HTMLButtonElement]]
        ] = None,
        on_load: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_load_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_load_start: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_load_start_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_loaded_data: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_loaded_data_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_loaded_metadata: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_loaded_metadata_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_lost_pointer_capture: Optional[
            EventType[()] | EventType[PointerEvent[HTMLButtonElement]]
        ] = None,
        on_lost_pointer_capture_capture: Optional[
            EventType[()] | EventType[PointerEvent[HTMLButtonElement]]
        ] = None,
        on_mouse_down: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_mouse_down_capture: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_mouse_enter: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_mouse_leave: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_mouse_move: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_mouse_move_capture: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_mouse_out: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_mouse_out_capture: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_mouse_over: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_mouse_over_capture: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_mouse_up: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_mouse_up_capture: Optional[
            EventType[()] | EventType[MouseEvent[HTMLButtonElement]]
        ] = None,
        on_paste: Optional[
            EventType[()] | EventType[ClipboardEvent[HTMLButtonElement]]
        ] = None,
        on_paste_capture: Optional[
            EventType[()] | EventType[ClipboardEvent[HTMLButtonElement]]
        ] = None,
        on_pause: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_pause_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_play: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_play_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_playing: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_playing_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_pointer_cancel: Optional[
            EventType[()] | EventType[PointerEvent[HTMLButtonElement]]
        ] = None,
        on_pointer_cancel_capture: Optional[
            EventType[()] | EventType[PointerEvent[HTMLButtonElement]]
        ] = None,
        on_pointer_down: Optional[
            EventType[()] | EventType[PointerEvent[HTMLButtonElement]]
        ] = None,
        on_pointer_down_capture: Optional[
            EventType[()] | EventType[PointerEvent[HTMLButtonElement]]
        ] = None,
        on_pointer_enter: Optional[
            EventType[()] | EventType[PointerEvent[HTMLButtonElement]]
        ] = None,
        on_pointer_leave: Optional[
            EventType[()] | EventType[PointerEvent[HTMLButtonElement]]
        ] = None,
        on_pointer_move: Optional[
            EventType[()] | EventType[PointerEvent[HTMLButtonElement]]
        ] = None,
        on_pointer_move_capture: Optional[
            EventType[()] | EventType[PointerEvent[HTMLButtonElement]]
        ] = None,
        on_pointer_out: Optional[
            EventType[()] | EventType[PointerEvent[HTMLButtonElement]]
        ] = None,
        on_pointer_out_capture: Optional[
            EventType[()] | EventType[PointerEvent[HTMLButtonElement]]
        ] = None,
        on_pointer_over: Optional[
            EventType[()] | EventType[PointerEvent[HTMLButtonElement]]
        ] = None,
        on_pointer_over_capture: Optional[
            EventType[()] | EventType[PointerEvent[HTMLButtonElement]]
        ] = None,
        on_pointer_up: Optional[
            EventType[()] | EventType[PointerEvent[HTMLButtonElement]]
        ] = None,
        on_pointer_up_capture: Optional[
            EventType[()] | EventType[PointerEvent[HTMLButtonElement]]
        ] = None,
        on_progress: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_progress_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_rate_change: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_rate_change_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_reset: Optional[
            EventType[()] | EventType[FormEvent[HTMLButtonElement]]
        ] = None,
        on_reset_capture: Optional[
            EventType[()] | EventType[FormEvent[HTMLButtonElement]]
        ] = None,
        on_resize: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_resize_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_scroll: Optional[
            EventType[()] | EventType[UIEvent[HTMLButtonElement]]
        ] = None,
        on_scroll_capture: Optional[
            EventType[()] | EventType[UIEvent[HTMLButtonElement]]
        ] = None,
        on_scroll_end: Optional[
            EventType[()] | EventType[UIEvent[HTMLButtonElement]]
        ] = None,
        on_scroll_end_capture: Optional[
            EventType[()] | EventType[UIEvent[HTMLButtonElement]]
        ] = None,
        on_seeked: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_seeked_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_seeking: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_seeking_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_select: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_select_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_stalled: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_stalled_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_submit: Optional[
            EventType[()] | EventType[FormEvent[HTMLButtonElement]]
        ] = None,
        on_submit_capture: Optional[
            EventType[()] | EventType[FormEvent[HTMLButtonElement]]
        ] = None,
        on_suspend: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_suspend_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_time_update: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_time_update_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_toggle: Optional[
            EventType[()] | EventType[ToggleEvent[HTMLButtonElement]]
        ] = None,
        on_touch_cancel: Optional[
            EventType[()] | EventType[TouchEvent[HTMLButtonElement]]
        ] = None,
        on_touch_cancel_capture: Optional[
            EventType[()] | EventType[TouchEvent[HTMLButtonElement]]
        ] = None,
        on_touch_end: Optional[
            EventType[()] | EventType[TouchEvent[HTMLButtonElement]]
        ] = None,
        on_touch_end_capture: Optional[
            EventType[()] | EventType[TouchEvent[HTMLButtonElement]]
        ] = None,
        on_touch_move: Optional[
            EventType[()] | EventType[TouchEvent[HTMLButtonElement]]
        ] = None,
        on_touch_move_capture: Optional[
            EventType[()] | EventType[TouchEvent[HTMLButtonElement]]
        ] = None,
        on_touch_start: Optional[
            EventType[()] | EventType[TouchEvent[HTMLButtonElement]]
        ] = None,
        on_touch_start_capture: Optional[
            EventType[()] | EventType[TouchEvent[HTMLButtonElement]]
        ] = None,
        on_transition_cancel: Optional[
            EventType[()] | EventType[TransitionEvent[HTMLButtonElement]]
        ] = None,
        on_transition_cancel_capture: Optional[
            EventType[()] | EventType[TransitionEvent[HTMLButtonElement]]
        ] = None,
        on_transition_end: Optional[
            EventType[()] | EventType[TransitionEvent[HTMLButtonElement]]
        ] = None,
        on_transition_end_capture: Optional[
            EventType[()] | EventType[TransitionEvent[HTMLButtonElement]]
        ] = None,
        on_transition_run: Optional[
            EventType[()] | EventType[TransitionEvent[HTMLButtonElement]]
        ] = None,
        on_transition_run_capture: Optional[
            EventType[()] | EventType[TransitionEvent[HTMLButtonElement]]
        ] = None,
        on_transition_start: Optional[
            EventType[()] | EventType[TransitionEvent[HTMLButtonElement]]
        ] = None,
        on_transition_start_capture: Optional[
            EventType[()] | EventType[TransitionEvent[HTMLButtonElement]]
        ] = None,
        on_volume_change: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_volume_change_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_waiting: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_waiting_capture: Optional[
            EventType[()] | EventType[SyntheticEvent[HTMLButtonElement]]
        ] = None,
        on_wheel: Optional[
            EventType[()] | EventType[WheelEvent[HTMLButtonElement]]
        ] = None,
        on_wheel_capture: Optional[
            EventType[()] | EventType[WheelEvent[HTMLButtonElement]]
        ] = None,
        **props,
    ) -> "Button":
        """Create the component.

        Args:
            *children: The children of the component.
            form_action: NOTE: rx.Var[support form_action callbacks?]
            default_checked: React-specific Attributes
            access_key: Standard HTML Attributes
            lang: id: rx.Var[str]
            tab_index: style: rx.Var[Dict[str, Any]]  # CSSProperties
            radio_group: Unknown
            about: RDFa Attributes
            auto_correct: Non-standard Attributes
            popover: Popover API
            inert: Living Standard  https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/inert
            input_mode: Hints at the type of data that might be entered by the user while editing the element or its contents  https://html.spec.whatwg.org/multipage/interaction.html#input-modalities:-the-inputmode-attribute
            is_: Specify that a standard HTML element should behave like a defined custom built-in element  https://html.spec.whatwg.org/multipage/custom-elements.html#attr-is
            exportparts: https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/exportparts
            part: https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/part
            on_copy: Clipboard Events
            on_composition_end: Composition Events
            on_focus: Focus Events
            on_change: Form Events  Special typing for on_change for <input>, <textarea>, and <select> elements
            on_load: Image Events (Usually SyntheticEvent)
            on_key_down: Keyboard Events
            on_key_up: on_key_press: rx.EventHandler[keyboard_handler] # deprecated  on_key_press_capture: rx.EventHandler[keyboard_handler] # deprecated
            on_abort: Media Events (Usually SyntheticEvent)
            on_aux_click: Mouse Events (Using pointer_event for consistency where applicable, mouse_event otherwise)
            on_select: Selection Events (Usually SyntheticEvent)
            on_touch_cancel: Touch Events
            on_pointer_down: Pointer Events
            on_scroll: UI Events (Usually UIEvent or SyntheticEvent)
            on_wheel: Wheel Events
            on_animation_start: Animation Events
            on_toggle: Toggle Events
            on_transition_cancel: Transition Events
            class_name: The class name for the component.
            **props: The props of the component.

        Returns:
            The component."""
        ...

button = Button.create
__all__ = ["button", "Button"]
