# Adapted from @types/react 19.0
# NOT the same thing as the properties in `elements.py` (but very similar)
from typing import Any, Dict, List, Literal, Union
import reflex as rx

from reflex_experiment.components.base import ComponentBase
from reflex_experiment.elements import (  # noqa: F401
    HTMLAnchorElement,
    HTMLAreaElement,
    HTMLAudioElement,
    HTMLBaseElement,
    HTMLButtonElement,
    HTMLDataElement,
    HTMLDetailsElement,
    HTMLDialogElement,
    HTMLElementBase,
    HTMLEmbedElement,
    HTMLFieldSetElement,
    HTMLFormElement,
    HTMLHtmlElement,
    HTMLIFrameElement,
    HTMLImageElement,
    HTMLInputElement,
    HTMLLabelElement,
    HTMLLiElement,
    HTMLLinkElement,
    HTMLMapElement,
    HTMLMediaElement,
    HTMLMenuElement,
    HTMLMetaElement,
    HTMLMeterElement,
    HTMLModElement,
    HTMLObjectElement,
    HTMLOListElement,
    HTMLOptGroupElement,
    HTMLOptionElement,
    HTMLOutputElement,
    HTMLProgressElement,
    HTMLQuoteElement,
    HTMLScriptElement,
    HTMLSelectElement,
    HTMLSlotElement,
    HTMLSourceElement,
    HTMLStyleElement,
    HTMLTableCaptionElement,
    HTMLTableCellElement,
    HTMLTableColElement,
    HTMLTableElement,
    HTMLTableRowElement,
    HTMLTableSectionElement,
    HTMLTextAreaElement,
    HTMLTimeElement,
    HTMLTrackElement,
    HTMLVideoElement,
)
from reflex_experiment.events import DOMEvents

Booleanish = Literal[True, False, "true", "false"]
CrossOrigin = Literal["anonymous", "use-credentials", ""] | None


# Note: we're going to redefine certain vars already set on rx.Component, but
# that will allow them to appear in the generated .pyi file with our custom
# pyi_generator
class HTMLAttributes(ComponentBase):
    # React-specific Attributes
    default_checked: rx.Var[bool]
    default_value: rx.Var[Union[str, int, List[str]]]
    suppress_content_editable_warning: rx.Var[bool]
    suppress_hydration_warning: rx.Var[bool]

    # Standard HTML Attributes
    access_key: rx.Var[str]
    auto_capitalize: rx.Var[
        Literal["off", "none", "on", "sentences", "words", "characters"]
    ]
    auto_focus: rx.Var[bool]
    class_name: rx.Var[str]  # type: ignore
    content_editable: rx.Var[Union[Booleanish, Literal["inherit", "plaintext-only"]]]
    context_menu: rx.Var[str]
    dir: rx.Var[str]
    draggable: rx.Var[Booleanish]
    enter_key_hint: rx.Var[
        Literal["enter", "done", "go", "next", "previous", "search", "send"]
    ]
    hidden: rx.Var[bool]
    id: rx.Var[str]  # type: ignore
    lang: rx.Var[str]
    nonce: rx.Var[str]
    slot: rx.Var[str]
    spell_check: rx.Var[Booleanish]
    style: rx.Var[Dict[str, Any]]  # type: ignore # CSSProperties
    tab_index: rx.Var[int]
    title: rx.Var[str]
    translate: rx.Var[Literal["yes", "no"]]

    # Unknown
    radio_group: rx.Var[str]  # <command>, <menuitem>

    # role: skipped

    # RDFa Attributes
    about: rx.Var[str]
    content: rx.Var[str]
    datatype: rx.Var[str]
    inlist: rx.Var[Any]
    prefix: rx.Var[str]
    property: rx.Var[str]
    rel: rx.Var[str]
    resource: rx.Var[str]
    rev: rx.Var[str]
    typeof: rx.Var[str]
    vocab: rx.Var[str]

    # Non-standard Attributes
    auto_correct: rx.Var[str]
    auto_save: rx.Var[str]
    color: rx.Var[str]
    item_prop: rx.Var[str]
    item_scope: rx.Var[bool]
    item_type: rx.Var[str]
    item_id: rx.Var[str]
    item_ref: rx.Var[str]
    results: rx.Var[int]
    security: rx.Var[str]
    unselectable: rx.Var[Literal["on", "off"]]

    # Popover API
    popover: rx.Var[Literal["", "auto", "manual"]]
    popover_target_action: rx.Var[Literal["toggle", "show", "hide"]]
    popover_target: rx.Var[str]

    # Living Standard
    # https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/inert
    inert: rx.Var[bool]
    # Hints at the type of data that might be entered by the user while editing the element or its contents
    # https://html.spec.whatwg.org/multipage/interaction.html#input-modalities:-the-inputmode-attribute
    input_mode: rx.Var[
        Literal["none", "text", "tel", "url", "email", "numeric", "decimal", "search"]
    ]

    # Specify that a standard HTML element should behave like a defined custom built-in element
    # https://html.spec.whatwg.org/multipage/custom-elements.html#attr-is
    is_: rx.Var[str]
    # https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/exportparts
    exportparts: rx.Var[str]
    # https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/part
    part: rx.Var[str]


HTMLAttributeReferrerPolicy = Literal[
    "",
    "no-referrer",
    "no-referrer-when-downgrade",
    "origin",
    "origin-when-cross-origin",
    "same-origin",
    "strict-origin",
    "strict-origin-when-cross-origin",
    "unsafe-url",
]


class HTMLAnchorProps(HTMLAttributes, DOMEvents[HTMLAnchorElement]):
    download: Any
    href: str
    href_lang: str
    media: str
    ping: str
    target: str
    type: str
    referrer_policy: HTMLAttributeReferrerPolicy


class HTMLAreaProps(HTMLAttributes, DOMEvents[HTMLAreaElement]):
    alt: str
    coords: str
    download: Any
    href: str
    href_lang: str
    media: str
    referrer_policy: HTMLAttributeReferrerPolicy
    shape: str
    target: str


class HTMLBaseProps(HTMLAttributes, DOMEvents[HTMLBaseElement]):
    href: str
    target: str


class HTMLBlockquoteProps(HTMLAttributes, DOMEvents[HTMLQuoteElement]):
    cite: str


class HTMLButtonProps(HTMLAttributes, DOMEvents[HTMLButtonElement]):
    disabled: rx.Var[bool]
    form: rx.Var[str]
    # NOTE: rx.Var[support form_action callbacks?]
    form_action: rx.Var[str]
    form_enc_type: rx.Var[str]
    form_method: rx.Var[str]
    form_no_validate: rx.Var[bool]
    form_target: rx.Var[str]
    name: rx.Var[str]
    type: rx.Var[Literal["submit", "reset", "button"]]
    value: rx.Var[Union[str, List[str], int]]


class HTMLCanvasProps(HTMLAttributes, DOMEvents[HTMLElementBase]):
    height: Union[int, str]
    width: Union[int, str]


class HTMLColProps(HTMLAttributes, DOMEvents[HTMLTableColElement]):
    span: int
    width: Union[int, str]


class HTMLColgroupProps(HTMLAttributes, DOMEvents[HTMLTableColElement]):
    span: int


class HTMLDataProps(HTMLAttributes, DOMEvents[HTMLDataElement]):
    value: Union[str, List[str], int]


class HTMLDetailsProps(HTMLAttributes, DOMEvents[HTMLDetailsElement]):
    open: bool
    name: str


class HTMLDelProps(HTMLAttributes, DOMEvents[HTMLModElement]):
    cite: str
    date_time: str


class HTMLDialogProps(HTMLAttributes, DOMEvents[HTMLDialogElement]):
    open: bool


class HTMLEmbedProps(HTMLAttributes, DOMEvents[HTMLEmbedElement]):
    height: Union[int, str]
    src: str
    type: str
    width: Union[int, str]


class HTMLFieldsetProps(HTMLAttributes, DOMEvents[HTMLFieldSetElement]):
    disabled: bool
    form: str
    name: str


class HTMLFormProps(HTMLAttributes, DOMEvents[HTMLFormElement]):
    accept_charset: str
    # NOTE: support action callbacks?
    action: str
    auto_complete: str
    enc_type: str
    method: str
    name: str
    no_validate: bool
    target: str


class HTMLHtmlProps(HTMLAttributes, DOMEvents[HTMLHtmlElement]):
    manifest: str


class HTMLIframeProps(HTMLAttributes, DOMEvents[HTMLIFrameElement]):
    allow: str
    allow_full_screen: bool
    allow_transparency: bool
    frame_border: Union[int, str]  # deprecated
    height: Union[int, str]
    loading: Literal["eager", "lazy"]
    margin_height: int  # deprecated
    margin_width: int  # deprecated
    name: str
    referrer_policy: HTMLAttributeReferrerPolicy
    sandbox: str
    scrolling: str  # deprecated
    seamless: bool
    src: str
    src_doc: str
    width: Union[int, str]


class HTMLImgProps(HTMLAttributes, DOMEvents[HTMLImageElement]):
    alt: str
    cross_origin: CrossOrigin
    decoding: Literal["async", "auto", "sync"]
    fetch_priority: Literal["high", "low", "auto"]
    height: Union[int, str]
    loading: Literal["eager", "lazy"]
    referrer_policy: HTMLAttributeReferrerPolicy
    sizes: str
    src: str
    src_set: str
    use_map: str
    width: Union[int, str]


class HTMLInsProps(HTMLAttributes, DOMEvents[HTMLModElement]):
    cite: str
    date_time: str


HTMLInputType = (
    Literal[
        "button",
        "checkbox",
        "color",
        "date",
        "datetime-local",
        "email",
        "file",
        "hidden",
        "image",
        "month",
        "number",
        "password",
        "radio",
        "range",
        "reset",
        "search",
        "submit",
        "tel",
        "text",
        "time",
        "url",
        "week",
    ]
    | str
)


class HTMLInputProps(HTMLAttributes, DOMEvents[HTMLInputElement]):
    accept: str
    alt: str
    auto_complete: str  # HTMLInputAutoCompleteAttribute
    capture: Union[bool, Literal["user", "environment"]]
    checked: bool
    disabled: bool
    form: str
    form_action: str
    form_enc_type: str
    form_method: str
    form_no_validate: bool
    form_target: str
    height: Union[int, str]
    list: str
    max: Union[int, str]
    max_length: int
    min: Union[int, str]
    min_length: int
    multiple: bool
    name: str
    pattern: str
    placeholder: str
    read_only: bool
    required: bool
    size: int
    src: str
    step: Union[int, str]
    type: HTMLInputType
    value: Union[str, List[str], int]
    width: Union[int, str]


class HTMLKeygenProps(HTMLAttributes, DOMEvents[HTMLElementBase]):
    challenge: str
    disabled: bool
    form: str
    key_type: str
    key_params: str
    name: str


class HTMLLabelProps(HTMLAttributes, DOMEvents[HTMLLabelElement]):
    form: str
    html_for: str


class HTMLLiProps(HTMLAttributes, DOMEvents[HTMLLiElement]):
    value: Union[str, List[str], int]


class HTMLLinkProps(HTMLAttributes, DOMEvents[HTMLLinkElement]):
    as_: str
    cross_origin: CrossOrigin
    fetch_priority: Literal["high", "low", "auto"]
    href: str
    href_lang: str
    integrity: str
    media: str
    image_src_set: str
    image_sizes: str
    referrer_policy: HTMLAttributeReferrerPolicy
    sizes: str
    type: str
    char_set: str
    precedence: str


class HTMLMapProps(HTMLAttributes, DOMEvents[HTMLMapElement]):
    name: str


class HTMLMenuProps(HTMLAttributes, DOMEvents[HTMLMenuElement]):
    type: str


class HTMLMediaProps(HTMLAttributes, DOMEvents[HTMLMediaElement]):
    auto_play: bool
    controls: bool
    controls_list: str
    cross_origin: CrossOrigin
    loop: bool
    media_group: str
    muted: bool
    plays_inline: bool
    preload: str
    src: str


# Note: not alphabetical order due to inheritance
class HTMLAudioProps(HTMLMediaProps, DOMEvents[HTMLAudioElement]):
    pass


class HTMLMetaProps(HTMLAttributes, DOMEvents[HTMLMetaElement]):
    char_set: str
    content: str
    http_equiv: str
    media: str
    name: str


class HTMLMeterProps(HTMLAttributes, DOMEvents[HTMLMeterElement]):
    form: str
    high: int
    low: int
    max: Union[int, str]
    min: Union[int, str]
    optimum: int
    value: Union[str, List[str], int]


class HTMLQuoteProps(HTMLAttributes, DOMEvents[HTMLQuoteElement]):
    cite: str


class HTMLObjectProps(HTMLAttributes, DOMEvents[HTMLObjectElement]):
    class_id: str
    data: str
    form: str
    height: Union[int, str]
    name: str
    type: str
    use_map: str
    width: Union[int, str]
    wmode: str


class HTMLOlProps(HTMLAttributes, DOMEvents[HTMLOListElement]):
    reversed: bool
    start: int
    type: Literal["1", "a", "A", "i", "I"]


class HTMLOptgroupProps(HTMLAttributes, DOMEvents[HTMLOptGroupElement]):
    disabled: bool
    label: str


class HTMLOptionProps(HTMLAttributes, DOMEvents[HTMLOptionElement]):
    disabled: bool
    label: str
    selected: bool
    value: Union[str, List[str], int]


class HTMLOutputProps(HTMLAttributes, DOMEvents[HTMLOutputElement]):
    form: str
    html_for: str
    name: str


class HTMLParamProps(HTMLAttributes, DOMEvents[HTMLElementBase]):
    name: str
    value: Union[str, List[str], int]


class HTMLProgressProps(HTMLAttributes, DOMEvents[HTMLProgressElement]):
    max: Union[int, str]
    value: Union[str, List[str], int]


class HTMLSlotProps(HTMLAttributes, DOMEvents[HTMLSlotElement]):
    name: str


class HTMLScriptProps(HTMLAttributes, DOMEvents[HTMLScriptElement]):
    async_: bool
    char_set: str  # deprecated
    cross_origin: CrossOrigin
    defer: bool
    integrity: str
    no_module: bool
    referrer_policy: HTMLAttributeReferrerPolicy
    src: str
    type: str


class HTMLSelectProps(HTMLAttributes, DOMEvents[HTMLSelectElement]):
    auto_complete: str
    disabled: bool
    form: str
    multiple: bool
    name: str
    required: bool
    size: int
    value: Union[str, List[str], int]


class HTMLSourceProps(HTMLAttributes, DOMEvents[HTMLSourceElement]):
    height: Union[int, str]
    media: str
    sizes: str
    src: str
    src_set: str
    type: str
    width: Union[int, str]


class HTMLStyleProps(HTMLAttributes, DOMEvents[HTMLStyleElement]):
    media: str
    scoped: bool
    type: str
    href: str
    precedence: str


class HTMLTableProps(HTMLAttributes, DOMEvents[HTMLTableElement]):
    align: Literal["left", "center", "right"]
    bgcolor: str
    border: int
    cell_padding: Union[int, str]
    cell_spacing: Union[int, str]
    frame: bool
    rules: Literal["none", "groups", "rows", "columns", "all"]
    summary: str
    width: Union[int, str]


class HTMLTextareaProps(HTMLAttributes, DOMEvents[HTMLTextAreaElement]):
    auto_complete: str
    cols: int
    dir_name: str
    disabled: bool
    form: str
    max_length: int
    min_length: int
    name: str
    placeholder: str
    read_only: bool
    required: bool
    rows: int
    value: Union[str, List[str], int]
    wrap: str


class HTMLTdProps(HTMLAttributes, DOMEvents[HTMLTableCellElement]):
    align: Literal["left", "center", "right", "justify", "char"]
    col_span: int
    headers: str
    row_span: int
    scope: str
    abbr: str
    height: Union[int, str]
    width: Union[int, str]
    valign: Literal["top", "middle", "bottom", "baseline"]


class HTMLThProps(HTMLAttributes, DOMEvents[HTMLTableCellElement]):
    align: Literal["left", "center", "right", "justify", "char"]
    col_span: int
    headers: str
    row_span: int
    scope: str
    abbr: str


class HTMLTimeProps(HTMLAttributes, DOMEvents[HTMLTimeElement]):
    date_time: str


class HTMLTrackProps(HTMLAttributes, DOMEvents[HTMLTrackElement]):
    default: bool
    kind: str
    label: str
    src: str
    src_lang: str


class HTMLVideoProps(HTMLMediaProps, DOMEvents[HTMLVideoElement]):
    height: Union[int, str]
    plays_inline: bool
    poster: str
    width: Union[int, str]
    disable_picture_in_picture: bool
    disable_remote_playback: bool


class SVGAttributes(ComponentBase):
    """SVG attributes supported by React"""

    # React-specific attributes
    suppress_hydration_warning: bool

    # Shared with HTMLAttributes
    class_name: str  # type: ignore
    color: str
    height: Union[int, str]
    id: str  # type: ignore
    lang: str
    max: Union[int, str]
    media: str
    method: str
    min: Union[int, str]
    name: str
    style: Dict[str, Any]  # type: ignore
    target: str
    type: str
    width: Union[int, str]

    # Other HTML properties
    role: str
    tab_index: int
    cross_origin: str

    # SVG specific attributes
    accent_height: Union[int, str]
    accumulate: Literal["none", "sum"]
    additive: Literal["replace", "sum"]
    alignment_baseline: rx.Var[
        Literal[
            "auto",
            "baseline",
            "before-edge",
            "text-before-edge",
            "middle",
            "central",
            "after-edge",
            "text-after-edge",
            "ideographic",
            "alphabetic",
            "hanging",
            "mathematical",
            "inherit",
        ]
    ]
    allow_reorder: Literal["no", "yes"]
    alphabetic: Union[int, str]
    amplitude: Union[int, str]
    arabic_form: Literal["initial", "medial", "terminal", "isolated"]
    ascent: Union[int, str]
    attribute_name: str
    attribute_type: str
    auto_reverse: bool
    azimuth: Union[int, str]
    base_frequency: Union[int, str]
    baseline_shift: Union[int, str]
    base_profile: Union[int, str]
    bbox: Union[int, str]
    begin: Union[int, str]
    bias: Union[int, str]
    by: Union[int, str]
    calc_mode: Union[int, str]
    cap_height: Union[int, str]
    clip: Union[int, str]
    clip_path: str
    clip_path_units: Union[int, str]
    clip_rule: Union[int, str]
    color_interpolation: Union[int, str]
    color_interpolation_filters: Literal["auto", "sRGB", "linearRGB", "inherit"]
    color_profile: Union[int, str]
    color_rendering: Union[int, str]
    content_script_type: Union[int, str]
    content_style_type: Union[int, str]
    cursor: Union[int, str]
    cx: Union[int, str]
    cy: Union[int, str]
    d: str
    decelerate: Union[int, str]
    descent: Union[int, str]
    diffuse_constant: Union[int, str]
    direction: Union[int, str]
    display: Union[int, str]
    divisor: Union[int, str]
    dominant_baseline: Union[int, str]
    dur: Union[int, str]
    dx: Union[int, str]
    dy: Union[int, str]
    edge_mode: Union[int, str]
    elevation: Union[int, str]
    enable_background: Union[int, str]
    end: Union[int, str]
    exponent: Union[int, str]
    external_resources_required: bool
    fill: str
    fill_opacity: Union[int, str]
    fill_rule: Literal["nonzero", "evenodd", "inherit"]
    filter: str
    filter_res: Union[int, str]
    filter_units: Union[int, str]
    flood_color: Union[int, str]
    flood_opacity: Union[int, str]
    focusable: Union[bool, Literal["auto"]]
    font_family: str
    font_size: Union[int, str]
    font_size_adjust: Union[int, str]
    font_stretch: Union[int, str]
    font_style: Union[int, str]
    font_variant: Union[int, str]
    font_weight: Union[int, str]
    format: Union[int, str]
    fr: Union[int, str]
    from_: Union[int, str]
    fx: Union[int, str]
    fy: Union[int, str]
    g1: Union[int, str]
    g2: Union[int, str]
    glyph_name: Union[int, str]
    glyph_orientation_horizontal: Union[int, str]
    glyph_orientation_vertical: Union[int, str]
    glyph_ref: Union[int, str]
    gradient_transform: str
    gradient_units: str
    hanging: Union[int, str]
    horiz_adv_x: Union[int, str]
    horiz_origin_x: Union[int, str]
    href: str
    ideographic: Union[int, str]
    image_rendering: Union[int, str]
    in2: Union[int, str]
    in_: str
    intercept: Union[int, str]
    k1: Union[int, str]
    k2: Union[int, str]
    k3: Union[int, str]
    k4: Union[int, str]
    k: Union[int, str]
    kernel_matrix: Union[int, str]
    kernel_unit_length: Union[int, str]
    kerning: Union[int, str]
    key_points: Union[int, str]
    key_splines: Union[int, str]
    key_times: Union[int, str]
    length_adjust: Union[int, str]
    letter_spacing: Union[int, str]
    lighting_color: Union[int, str]
    limiting_cone_angle: Union[int, str]
    local: Union[int, str]
    marker_end: str
    marker_height: Union[int, str]
    marker_mid: str
    marker_start: str
    marker_units: Union[int, str]
    marker_width: Union[int, str]
    mask: str
    mask_content_units: Union[int, str]
    mask_units: Union[int, str]
    mathematical: Union[int, str]
    mode: Union[int, str]
    num_octaves: Union[int, str]
    offset: Union[int, str]
    opacity: Union[int, str]
    operator: Union[int, str]
    order: Union[int, str]
    orient: Union[int, str]
    orientation: Union[int, str]
    origin: Union[int, str]
    overflow: Union[int, str]
    overline_position: Union[int, str]
    overline_thickness: Union[int, str]
    paint_order: Union[int, str]
    panose1: Union[int, str]
    path: str
    path_length: Union[int, str]
    pattern_content_units: str
    pattern_transform: Union[int, str]
    pattern_units: str
    pointer_events: Union[int, str]
    points: str
    points_at_x: Union[int, str]
    points_at_y: Union[int, str]
    points_at_z: Union[int, str]
    preserve_alpha: bool
    preserve_aspect_ratio: str
    primitive_units: Union[int, str]
    r: Union[int, str]
    radius: Union[int, str]
    ref_x: Union[int, str]
    ref_y: Union[int, str]
    rendering_intent: Union[int, str]
    repeat_count: Union[int, str]
    repeat_dur: Union[int, str]
    required_extensions: Union[int, str]
    required_features: Union[int, str]
    restart: Union[int, str]
    result: str
    rotate: Union[int, str]
    rx: Union[int, str]
    ry: Union[int, str]
    scale: Union[int, str]
    seed: Union[int, str]
    shape_rendering: Union[int, str]
    slope: Union[int, str]
    spacing: Union[int, str]
    specular_constant: Union[int, str]
    specular_exponent: Union[int, str]
    speed: Union[int, str]
    spread_method: str
    start_offset: Union[int, str]
    std_deviation: Union[int, str]
    stemh: Union[int, str]
    stemv: Union[int, str]
    stitch_tiles: Union[int, str]
    stop_color: str
    stop_opacity: Union[int, str]
    strikethrough_position: Union[int, str]
    strikethrough_thickness: Union[int, str]
    string: Union[int, str]
    stroke: str
    stroke_dasharray: Union[int, str]
    stroke_dashoffset: Union[int, str]
    stroke_linecap: Literal["butt", "round", "square", "inherit"]
    stroke_linejoin: Literal["miter", "round", "bevel", "inherit"]
    stroke_miterlimit: Union[int, str]
    stroke_opacity: Union[int, str]
    stroke_width: Union[int, str]
    surface_scale: Union[int, str]
    system_language: Union[int, str]
    table_values: Union[int, str]
    target_x: Union[int, str]
    target_y: Union[int, str]
    text_anchor: str
    text_decoration: Union[int, str]
    text_length: Union[int, str]
    text_rendering: Union[int, str]
    to: Union[int, str]
    transform: str
    u1: Union[int, str]
    u2: Union[int, str]
    underline_position: Union[int, str]
    underline_thickness: Union[int, str]
    unicode: Union[int, str]
    unicode_bidi: Union[int, str]
    unicode_range: Union[int, str]
    units_per_em: Union[int, str]
    v_alphabetic: Union[int, str]
    values: str
    vector_effect: Union[int, str]
    version: str
    vert_adv_y: Union[int, str]
    vert_origin_x: Union[int, str]
    vert_origin_y: Union[int, str]
    v_hanging: Union[int, str]
    v_ideographic: Union[int, str]
    view_box: str
    view_target: Union[int, str]
    visibility: Union[int, str]
    v_mathematical: Union[int, str]
    widths: Union[int, str]
    word_spacing: Union[int, str]
    writing_mode: Union[int, str]
    x1: Union[int, str]
    x2: Union[int, str]
    x: Union[int, str]
    x_channel_selector: str
    x_height: Union[int, str]
    xlink_actuate: str
    xlink_arcrole: str
    xlink_href: str
    xlink_role: str
    xlink_show: str
    xlink_title: str
    xlink_type: str
    xml_base: str
    xml_lang: str
    xmlns: str
    xmlns_xlink: str
    xml_space: str
    y1: Union[int, str]
    y2: Union[int, str]
    y: Union[int, str]
    y_channel_selector: str
    z: Union[int, str]
    zoom_and_pan: str


class WebViewAttributes(HTMLAttributes):
    allow_full_screen: bool
    allowpopups: bool
    autosize: bool
    blinkfeatures: str
    disableblinkfeatures: str
    disableguestresize: bool
    disablewebsecurity: bool
    guestinstance: str
    httpreferrer: str
    nodeintegration: bool
    partition: str
    plugins: bool
    preload: str
    src: str
    useragent: str
    webpreferences: str
