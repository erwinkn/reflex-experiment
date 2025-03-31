# Adapted from MDN Web Docs and @types/react Note: Similar to events, we can
# only serialize data attributes, not methods or complex objects like NodeList.
# We primarily focus on properties useful to the backend (like the position of
# an element, its size, or its value).

from typing import Any, Literal, Optional, Union, Dict
import reflex as rx
from pydantic.v1 import Field


# rx.Base is a wrapper around a Pydantic v1 Model


class Element(rx.Base):
    # Basic properties
    id: str
    class_name: str
    tag_name: str
    local_name: str
    client_height: float
    client_left: float
    client_top: float
    client_width: float
    scroll_height: float
    scroll_left: float
    scroll_top: float
    scroll_width: float
    slot: str

    # Not including innerHTML and outerHTML as those could be heavy


class HTMLOrSVGElement(rx.Base):
    autofocus: bool
    tab_index: int
    nonce: Optional[str]


class BaseHTMLElement(Element, HTMLOrSVGElement):
    access_key: str
    access_key_label: str
    autocapitalize: str
    dir: Literal["ltr", "rtl", "auto"]
    draggable: bool
    hidden: bool
    inert: bool
    lang: str

    offset_height: float  # Read-only layout properties
    offset_left: float
    # offset_parent: Element | None # could be complex to serialize
    offset_top: float
    offset_width: float
    popover: Optional[str]
    spellcheck: bool
    title: str
    translate: bool
    writing_suggestions: str

    # Added properties from HTMLElement definition
    content_editable: str
    enter_key_hint: str
    is_content_editable: bool
    input_mode: str
    dataset: Dict[str, str]

    # Not including inner_text and outer_text as those could be heavy


class HTMLAnchorElement(BaseHTMLElement):
    """Properties specific to <a> elements."""

    tag_name: Literal["a"]

    hash: str
    host: str
    hostname: str
    href: str
    origin: str
    password: str
    pathname: str
    port: str
    protocol: str
    search: str
    target: str
    download: str
    rel: str
    hreflang: str
    type: str
    username: str

    # Added properties
    ping: str
    referrer_policy: Literal[
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
    text: str


class HTMLAreaElement(BaseHTMLElement):
    """Properties specific to <area> elements."""

    tag_name: Literal["area"]

    alt: str
    coords: str
    download: str
    hash: str
    host: str
    hostname: str
    href: str
    origin: str
    password: str
    pathname: str
    port: str
    protocol: str
    rel: str
    search: str
    shape: str
    target: str
    username: str

    # Added properties
    ping: str
    referrer_policy: Literal[
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


class HTMLMediaElement(BaseHTMLElement):
    """Properties specific to media elements like <audio> and <video>."""

    autoplay: bool
    controls: bool
    cross_origin: Optional[Literal["anonymous", "use-credentials"]]
    current_src: str
    current_time: float
    default_muted: bool
    default_playback_rate: float
    duration: float  # Read-only, NaN if unavailable
    ended: bool  # Read-only
    loop: bool
    muted: bool
    network_state: Literal[
        0, 1, 2, 3
    ]  # NETWORK_EMPTY, NETWORK_IDLE, NETWORK_LOADING, NETWORK_NO_SOURCE
    paused: bool  # Read-only
    playback_rate: float
    preload: Literal["none", "metadata", "auto", ""]
    ready_state: Literal[0, 1, 2, 3, 4]
    seeking: bool  # Read-only
    src: str
    volume: float
    preserves_pitch: bool


class HTMLAudioElement(HTMLMediaElement):
    """Specifies <audio> elements. Currently no differing properties from HTMLMediaElement in this subset."""

    tag_name: Literal["audio"]


class HTMLButtonElement(BaseHTMLElement):
    """Properties specific to <button> elements."""

    tag_name: Literal["button"]

    disabled: bool
    name: str
    type: Literal["submit", "reset", "button"]
    value: str

    # Added form-related attributes
    form_action: str
    form_enctype: str
    form_method: str
    form_no_validate: bool
    form_target: str
    popover_target_action: str


class HTMLDataElement(BaseHTMLElement):
    """Properties specific to <data> elements."""

    tag_name: Literal["data"]

    value: str


class HTMLEmbedElement(BaseHTMLElement):
    """Properties specific to <embed> elements."""

    tag_name: Literal["embed"]

    height: str
    src: str
    type: str
    width: str

    # Added deprecated properties
    align: str
    name: str


class HTMLFieldSetElement(BaseHTMLElement):
    """Properties specific to <fieldset> elements."""

    tag_name: Literal["fieldset"]

    disabled: bool
    name: str
    type: str  # Generally "fieldset"

    # Added validation properties
    validation_message: str
    will_validate: bool


class HTMLFormElement(BaseHTMLElement):
    """Properties specific to <form> elements."""

    tag_name: Literal["form"]

    accept_charset: str
    action: str
    autocomplete: Literal["on", "off"]
    encoding: str  # alias for enctype
    enctype: Literal[
        "application/x-www-form-urlencoded",
        "multipart/form-data",
        "text/plain",
    ]
    length: int  # Read-only, number of controls in the form
    method: Literal["get", "post", "dialog"]
    name: str
    no_validate: bool
    target: str
    rel: str


class HTMLIFrameElement(BaseHTMLElement):
    """Properties specific to <iframe> elements."""

    tag_name: Literal["iframe"]

    allow: str
    allow_fullscreen: bool
    height: str
    name: str
    referrer_policy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    src: str
    srcdoc: str
    width: str

    # Added deprecated properties
    align: str
    frame_border: str
    long_desc: str
    margin_height: str
    margin_width: str
    scrolling: str
    sandbox: str


class HTMLImageElement(BaseHTMLElement):
    """Properties specific to <img> elements."""

    tag_name: Literal["img"]

    alt: str
    cross_origin: Optional[Literal["anonymous", "use-credentials"]]
    decoding: Literal["sync", "async", "auto"]
    height: int
    is_map: bool
    loading: Literal["eager", "lazy"]
    natural_height: int  # Read-only, intrinsic height
    natural_width: int  # Read-only, intrinsic width
    referrer_policy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    sizes: str
    src: str
    srcset: str
    use_map: str
    width: int

    # Added properties (some deprecated)
    align: str
    border: str
    complete: bool
    hspace: int
    long_desc: str
    lowsrc: str
    name: str
    vspace: int
    x: float
    y: float
    fetch_priority: Literal["high", "low", "auto"]


class HTMLInputElement(BaseHTMLElement):
    """Properties specific to <input> elements."""

    tag_name: Literal["input"]

    accept: str
    alt: str
    autocomplete: str
    checked: bool  # For checkbox/radio
    default_checked: bool
    default_value: str
    dir_name: str
    disabled: bool
    height: str  # Only for type="image"
    indeterminate: bool  # For checkbox
    max: str  # Works with number, date, range types etc.
    max_length: int
    min: str
    min_length: int
    multiple: bool  # For email, file
    name: str
    pattern: str
    placeholder: str
    read_only: bool
    required: bool
    selection_direction: Optional[Literal["forward", "backward", "none"]]
    selection_end: Optional[int]
    selection_start: Optional[int]
    size: int
    src: str  # Only for type="image"
    step: str
    type: str  # Input type (text, password, checkbox, etc.)
    value: str  # Current value
    value_as_number: Optional[float]  # Parses value as float, NaN if invalid
    width: str  # Only for type="image"

    # Added properties (some deprecated)
    align: str
    capture: str
    form_action: str
    form_enctype: str
    form_method: str
    form_no_validate: bool
    form_target: str
    use_map: str
    validation_message: str
    will_validate: bool
    popover_target_action: str


class HTMLLabelElement(BaseHTMLElement):
    """Properties specific to <label> elements."""

    tag_name: Literal["label"]

    html_for: str  # Corresponds to 'for' attribute


class HTMLLiElement(BaseHTMLElement):
    """Properties specific to <li> elements."""

    tag_name: Literal["li"]

    value: int  # Only valid if parent is <ol>
    type: str


class HTMLLinkElement(BaseHTMLElement):
    """Properties specific to <link> elements."""

    tag_name: Literal["link"]

    as_: str  # Corresponds to 'as' attribute
    cross_origin: Optional[Literal["anonymous", "use-credentials"]]
    disabled: bool
    fetch_priority: Literal["high", "low", "auto"]
    href: str
    hreflang: str
    image_sizes: str
    image_srcset: str
    integrity: str
    media: str
    referrer_policy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    rel: str
    type: str

    # Added properties (some deprecated)
    charset: str
    rev: str
    target: str
    sizes: str


class HTMLMapElement(BaseHTMLElement):
    """Properties specific to <map> elements."""

    tag_name: Literal["map"]

    name: str


class HTMLMeterElement(BaseHTMLElement):
    """Properties specific to <meter> elements."""

    tag_name: Literal["meter"]

    high: float
    low: float
    max: float
    min: float
    optimum: float
    value: float


class HTMLModElement(BaseHTMLElement):
    """Properties specific to <ins> and <del> elements."""

    tag_name: Literal["ins", "del"]

    cite: str
    date_time: str  # Corresponds to 'datetime' attribute


class HTMLOListElement(BaseHTMLElement):
    """Properties specific to <ol> elements."""

    tag_name: Literal["ol"]

    reversed: bool
    start: int
    type: Literal["1", "a", "A", "i", "I"]
    compact: bool


class HTMLObjectElement(BaseHTMLElement):
    """Properties specific to <object> elements."""

    tag_name: Literal["object"]

    data: str
    disabled: bool
    height: str
    name: str
    type: str
    use_map: str
    width: str

    # Added properties (some deprecated)
    align: str
    archive: str
    border: str
    code: str
    code_base: str
    code_type: str
    declare: bool
    hspace: int
    standby: str
    validation_message: str
    vspace: int
    will_validate: bool


class HTMLOptGroupElement(BaseHTMLElement):
    """Properties specific to <optgroup> elements."""

    tag_name: Literal["optgroup"]

    disabled: bool
    label: str


class HTMLOptionElement(BaseHTMLElement):
    """Properties specific to <option> elements."""

    tag_name: Literal["option"]

    default_selected: bool
    disabled: bool
    index: int  # Read-only
    label: str
    selected: bool
    text: str  # Text content
    value: str


class HTMLOutputElement(BaseHTMLElement):
    """Properties specific to <output> elements."""

    tag_name: Literal["output"]

    default_value: str
    name: str
    type: str  # Generally "output"
    value: str

    # Added properties
    html_for: str
    validation_message: str
    will_validate: bool


class HTMLProgressElement(BaseHTMLElement):
    """Properties specific to <progress> elements."""

    tag_name: Literal["progress"]

    max: float
    position: float  # Read-only, -1 if indeterminate
    value: float


class HTMLQuoteElement(BaseHTMLElement):
    """Properties specific to <q> and <blockquote> elements."""

    tag_name: Literal["q", "blockquote"]

    cite: str


class HTMLCiteElement(BaseHTMLElement):
    """Properties specific to <cite> elements."""

    tag_name: Literal["cite"]


class HTMLScriptElement(BaseHTMLElement):
    """Properties specific to <script> elements."""

    tag_name: Literal["script"]

    async_: bool  # Corresponds to 'async' attribute
    cross_origin: Optional[Literal["anonymous", "use-credentials"]]
    defer: bool
    fetch_priority: Literal["high", "low", "auto"]
    integrity: str
    no_module: bool
    referrer_policy: Literal[
        "",
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]  # Expanded Literal
    src: str
    text: str  # Script content if inline
    type: str

    # Added deprecated properties
    charset: str
    event: str
    html_for: str


class HTMLSelectElement(BaseHTMLElement):
    """Properties specific to <select> elements."""

    tag_name: Literal["select"]

    autocomplete: str
    disabled: bool
    length: int  # Read-only, number of options
    multiple: bool
    name: str
    required: bool
    selected_index: int
    size: int
    type: Literal["select-one", "select-multiple"]  # Read-only
    value: str  # Value of the first selected option, or ""

    # Added validation properties
    validation_message: str
    will_validate: bool


class HTMLSlotElement(BaseHTMLElement):
    """Properties specific to <slot> elements."""

    tag_name: Literal["slot"]

    name: str


class HTMLSourceElement(BaseHTMLElement):
    """Properties specific to <source> elements."""

    tag_name: Literal["source"]

    height: int
    media: str
    sizes: str
    src: str
    srcset: str
    type: str
    width: int


class HTMLTableCaptionElement(BaseHTMLElement):
    """Properties specific to <caption> elements."""

    tag_name: Literal["caption"]
    align: str


class HTMLTableCellElement(BaseHTMLElement):
    """Properties specific to <td> and <th> elements."""

    tag_name: Literal["td", "th"]

    abbr: str
    cell_index: int  # Read-only
    col_span: int
    headers: str  # Corresponds to 'headers' attribute, space-separated list of IDs
    row_span: int
    scope: Literal["row", "col", "rowgroup", "colgroup", ""]

    # Added deprecated properties
    align: str
    axis: str
    bg_color: str
    ch: str
    ch_off: str
    height: str
    no_wrap: bool
    v_align: str
    width: str


class HTMLTableColElement(BaseHTMLElement):
    """Properties specific to <col> and <colgroup> elements."""

    tag_name: Literal["col", "colgroup"]

    span: int

    # Added deprecated properties
    align: str
    ch: str
    ch_off: str
    v_align: str
    width: str


class HTMLTableElement(BaseHTMLElement):
    """Properties specific to <table> elements."""

    tag_name: Literal["table"]

    caption: Optional[HTMLTableCaptionElement]  # Reference, might be tricky
    # t_head: Optional[HTMLTableSectionElement] # Reference
    # t_foot: Optional[HTMLTableSectionElement] # Reference
    # t_bodies: HTMLCollection # Cannot serialize
    # rows: HTMLCollection # Cannot serialize

    # Added deprecated properties
    align: str
    bg_color: str
    border: str
    cell_padding: str
    cell_spacing: str
    frame: str
    rules: str
    summary: str
    width: str


class HTMLTableRowElement(BaseHTMLElement):
    """Properties specific to <tr> elements."""

    tag_name: Literal["tr"]

    # cells: HTMLCollection # Cannot serialize
    row_index: int  # Read-only
    section_row_index: int  # Read-only

    # Added deprecated properties
    align: str
    bg_color: str
    ch: str
    ch_off: str
    v_align: str


class HTMLTableSectionElement(BaseHTMLElement):
    """Properties specific to <thead>, <tbody>, <tfoot> elements."""

    tag_name: Literal["thead", "tbody", "tfoot"]

    # rows: HTMLCollection # Cannot serialize
    # Added deprecated properties
    align: str
    ch: str
    ch_off: str
    v_align: str


class HTMLTemplateElement(BaseHTMLElement):
    """Properties specific to <template> elements."""

    tag_name: Literal["template"]

    # content: DocumentFragment # Cannot serialize
    pass


class HTMLTextAreaElement(BaseHTMLElement):
    """Properties specific to <textarea> elements."""

    tag_name: Literal["textarea"]

    autocomplete: str
    cols: int
    default_value: str
    dir_name: str
    disabled: bool
    max_length: int
    min_length: int
    name: str
    placeholder: str
    read_only: bool
    required: bool
    rows: int
    selection_direction: Optional[Literal["forward", "backward", "none"]]
    selection_end: Optional[int]
    selection_start: Optional[int]
    value: str
    wrap: Literal["soft", "hard", "off"]

    # Added properties
    text_length: int
    validation_message: str
    will_validate: bool


class HTMLTimeElement(BaseHTMLElement):
    """Properties specific to <time> elements."""

    tag_name: Literal["time"]

    date_time: str  # Corresponds to 'datetime' attribute


class HTMLTrackElement(BaseHTMLElement):
    """Properties specific to <track> elements."""

    tag_name: Literal["track"]

    default: bool
    kind: Literal["subtitles", "captions", "descriptions", "chapters", "metadata"]
    label: str
    ready_state: Literal[0, 1, 2, 3]
    src: str
    srclang: str
    # track: Optional[TextTrack] # Cannot serialize


class HTMLVideoElement(HTMLMediaElement):
    """Properties specific to <video> elements."""

    tag_name: Literal["video"]

    height: int
    poster: str
    video_height: int  # Read-only, intrinsic height
    video_width: int  # Read-only, intrinsic width
    width: int
    plays_inline: bool


class HTMLBRElement(BaseHTMLElement):
    """Properties specific to <br> elements."""

    tag_name: Literal["br"]
    clear: str


class HTMLBaseElement(BaseHTMLElement):
    """Properties specific to <base> elements."""

    tag_name: Literal["base"]
    href: str
    target: str


class HTMLBodyElement(BaseHTMLElement):
    """Properties specific to <body> elements."""

    tag_name: Literal["body"]
    a_link: str
    background: str
    bg_color: str
    link: str
    text: str
    v_link: str


class HTMLDListElement(BaseHTMLElement):
    """Properties specific to <dl> elements."""

    tag_name: Literal["dl"]
    compact: bool


class HTMLDetailsElement(BaseHTMLElement):
    """Properties specific to <details> elements."""

    tag_name: Literal["details"]
    open: bool


class HTMLDialogElement(BaseHTMLElement):
    """Properties specific to <dialog> elements."""

    tag_name: Literal["dialog"]
    open: bool
    return_value: str


class HTMLDivElement(BaseHTMLElement):
    """Properties specific to <div> elements."""

    tag_name: Literal["div"]
    align: str


class HTMLHeadElement(BaseHTMLElement):
    """Properties specific to <head> elements."""

    tag_name: Literal["head"]


class HTMLHeadingElement(BaseHTMLElement):
    """Properties specific to <h1> through <h6> elements."""

    tag_name: Literal["h1", "h2", "h3", "h4", "h5", "h6"]
    align: str


class HTMLHRElement(BaseHTMLElement):
    """Properties specific to <hr> elements."""

    tag_name: Literal["hr"]
    align: str
    color: str
    no_shade: bool
    size: str
    width: str


class HTMLHtmlElement(BaseHTMLElement):
    """Properties specific to <html> elements."""

    tag_name: Literal["html"]
    version: str


class HTMLMenuElement(BaseHTMLElement):
    """Properties specific to <menu> elements."""

    tag_name: Literal["menu"]


class HTMLMetaElement(BaseHTMLElement):
    """Properties specific to <meta> elements."""

    tag_name: Literal["meta"]
    content: str
    http_equiv: str
    name: str
    scheme: str


class HTMLParagraphElement(BaseHTMLElement):
    """Properties specific to <p> elements."""

    tag_name: Literal["p"]
    align: str


class HTMLPictureElement(BaseHTMLElement):
    """Properties specific to <picture> elements."""

    tag_name: Literal["picture"]


class HTMLPreElement(BaseHTMLElement):
    """Properties specific to <pre> elements."""

    tag_name: Literal["pre"]
    width: int


class HTMLSpanElement(BaseHTMLElement):
    """Properties specific to <span> elements."""

    tag_name: Literal["span"]
    # No additional properties


class HTMLStyleElement(BaseHTMLElement):
    """Properties specific to <style> elements."""

    tag_name: Literal["style"]
    media: str
    type: str
    disabled: bool


class HTMLTitleElement(BaseHTMLElement):
    """Properties specific to <title> elements."""

    tag_name: Literal["title"]
    text: str


class HTMLUListElement(BaseHTMLElement):
    """Properties specific to <ul> elements."""

    tag_name: Literal["ul"]
    compact: bool
    type: str


HTMLElement = Union[
    HTMLAnchorElement,
    HTMLAreaElement,
    HTMLAudioElement,
    HTMLBaseElement,
    HTMLBodyElement,
    HTMLBRElement,
    HTMLButtonElement,
    HTMLCiteElement,
    HTMLDataElement,
    HTMLDetailsElement,
    HTMLDialogElement,
    HTMLDivElement,
    HTMLDListElement,
    HTMLEmbedElement,
    HTMLFieldSetElement,
    HTMLFormElement,
    HTMLHeadElement,
    HTMLHeadingElement,
    HTMLHRElement,
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
    HTMLOListElement,
    HTMLObjectElement,
    HTMLOptGroupElement,
    HTMLOptionElement,
    HTMLOutputElement,
    HTMLParagraphElement,
    HTMLPictureElement,
    HTMLPreElement,
    HTMLProgressElement,
    HTMLQuoteElement,
    HTMLScriptElement,
    HTMLSelectElement,
    HTMLSlotElement,
    HTMLSourceElement,
    HTMLSpanElement,
    HTMLStyleElement,
    HTMLTableCaptionElement,
    HTMLTableCellElement,
    HTMLTableColElement,
    HTMLTableElement,
    HTMLTableRowElement,
    HTMLTableSectionElement,
    HTMLTemplateElement,
    HTMLTextAreaElement,
    HTMLTimeElement,
    HTMLTitleElement,
    HTMLTrackElement,
    HTMLUListElement,
    HTMLVideoElement,
]

HTMLElementField = Field(HTMLElement, discriminator="tag_name")
