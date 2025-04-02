/* === IMPORTANT === 
/* The contents of this file
*/

import { SyntheticEvent } from "react";

// used for untyped stuff, like nativeEvent
export function cleanForSerialization(obj: unknown) {
  const result = _cleanForSerializationRecursive(obj, new WeakSet());
  return result;
}

function _cleanForSerializationRecursive(obj: unknown, seen: WeakSet<WeakKey>) {
  if (obj === null || typeof obj !== "object") {
    return obj;
  }
  if (seen.has(obj)) {
    return undefined; // handle circular refs
  }

  seen.add(obj);

  if (Array.isArray(obj)) {
    const cleanedArray = obj
      .map((item) => _cleanForSerializationRecursive(item, seen))
      .filter((item) => item !== undefined);

    return cleanedArray;
  }

  const plainObject = {};

  for (const key in obj) {
    const value = obj[key];

    if (typeof key !== "string") {
      continue;
    }
    if (
      typeof value === "function" ||
      typeof value === "symbol" ||
      typeof value === "undefined"
    ) {
      continue;
    }

    const cleanedValue = _cleanForSerializationRecursive(value, seen);
    if (key === "target") {
      console.log("Cleaned target value:", cleanedValue);
    }
    if (cleanedValue !== undefined) {
      plainObject[key] = cleanedValue;
    }
  }

  return plainObject;
}

export function extractElement(elt: Element): object {
  return {
    id: elt.id,
    class_name: elt.className,
    tag_name: elt.tagName,
    local_name: elt.localName,
    client_height: elt.clientHeight,
    client_left: elt.clientLeft,
    client_top: elt.clientTop,
    client_width: elt.clientWidth,
    scroll_height: elt.scrollHeight,
    scroll_left: elt.scrollLeft,
    scroll_top: elt.scrollTop,
    scroll_width: elt.scrollWidth,
    slot: elt.slot,
  };
}

export function extractHTMLOrSVGElement(elt: HTMLOrSVGElement) {
  return {
    autofocus: elt.autofocus,
    tab_index: elt.tabIndex,
    nonce: elt.nonce,
  };
}

export function extractHTMLElementBase(elt: HTMLElement) {
  return {
    ...extractElement(elt),
    ...extractHTMLOrSVGElement(elt),
    access_key: elt.accessKey,
    access_key_label: elt.accessKeyLabel,
    autocapitalize: elt.autocapitalize,
    dir: elt.dir,
    draggable: elt.draggable,
    hidden: elt.hidden,
    inert: elt.inert,
    lang: elt.lang,
    offset_height: elt.offsetHeight,
    offset_left: elt.offsetLeft,
    offset_top: elt.offsetTop,
    offset_width: elt.offsetWidth,
    popover: elt.popover,
    spellcheck: elt.spellcheck,
    title: elt.title,
    translate: elt.translate,
    writing_suggestions: elt.writingSuggestions,
    content_editable: elt.contentEditable,
    enter_key_hint: elt.enterKeyHint,
    is_content_editable: elt.isContentEditable,
    input_mode: elt.inputMode,
  };
}

export function extractHTMLAnchorElement(elt: HTMLAnchorElement) {
  return {
    ...extractHTMLElementBase(elt),
    hash: elt.hash,
    host: elt.host,
    hostname: elt.hostname,
    href: elt.href,
    origin: elt.origin,
    password: elt.password,
    pathname: elt.pathname,
    port: elt.port,
    protocol: elt.protocol,
    search: elt.search,
    target: elt.target,
    download: elt.download,
    rel: elt.rel,
    hreflang: elt.hreflang,
    type: elt.type,
    username: elt.username,
    ping: elt.ping,
    referrerPolicy: elt.referrerPolicy,
    text: elt.text,
  };
}

export function extractHTMLAreaElement(elt: HTMLAreaElement) {
  return {
    ...extractHTMLElementBase(elt),
    alt: elt.alt,
    coords: elt.coords,
    download: elt.download,
    hash: elt.hash,
    host: elt.host,
    hostname: elt.hostname,
    href: elt.href,
    origin: elt.origin,
    password: elt.password,
    pathname: elt.pathname,
    port: elt.port,
    protocol: elt.protocol,
    rel: elt.rel,
    search: elt.search,
    shape: elt.shape,
    target: elt.target,
    username: elt.username,
    ping: elt.ping,
    referrerPolicy: elt.referrerPolicy,
  };
}

export function extractHTMLMediaElement(elt: HTMLMediaElement) {
  return {
    ...extractHTMLElementBase(elt),
    autoplay: elt.autoplay,
    controls: elt.controls,
    crossOrigin: elt.crossOrigin,
    currentSrc: elt.currentSrc,
    currentTime: elt.currentTime,
    defaultMuted: elt.defaultMuted,
    defaultPlaybackRate: elt.defaultPlaybackRate,
    duration: elt.duration,
    ended: elt.ended,
    loop: elt.loop,
    muted: elt.muted,
    networkState: elt.networkState,
    paused: elt.paused,
    playbackRate: elt.playbackRate,
    preload: elt.preload,
    readyState: elt.readyState,
    seeking: elt.seeking,
    src: elt.src,
    volume: elt.volume,
    preservesPitch: elt.preservesPitch,
  };
}

export function extractHTMLAudioElement(elt: HTMLAudioElement) {
  return {
    ...extractHTMLMediaElement(elt),
    // No additional properties for audio elements
  };
}

export function extractHTMLButtonElement(elt: HTMLButtonElement) {
  return {
    ...extractHTMLElementBase(elt),
    disabled: elt.disabled,
    name: elt.name,
    type: elt.type,
    value: elt.value,
    formAction: elt.formAction,
    formEnctype: elt.formEnctype,
    formMethod: elt.formMethod,
    formNoValidate: elt.formNoValidate,
    formTarget: elt.formTarget,
    popoverTargetAction: elt.popoverTargetAction,
  };
}

export function extractHTMLDataElement(elt: HTMLDataElement) {
  return {
    ...extractHTMLElementBase(elt),
    value: elt.value,
  };
}

export function extractHTMLEmbedElement(elt: HTMLEmbedElement) {
  return {
    ...extractHTMLElementBase(elt),
    height: elt.height,
    src: elt.src,
    type: elt.type,
    width: elt.width,
    align: elt.align,
    name: elt.name,
  };
}

export function extractHTMLFieldSetElement(elt: HTMLFieldSetElement) {
  return {
    ...extractHTMLElementBase(elt),
    disabled: elt.disabled,
    name: elt.name,
    type: elt.type,
    validationMessage: elt.validationMessage,
    willValidate: elt.willValidate,
  };
}

export function extractHTMLFormElement(elt: HTMLFormElement) {
  return {
    ...extractHTMLElementBase(elt),
    acceptCharset: elt.acceptCharset,
    action: elt.action,
    autocomplete: elt.autocomplete,
    encoding: elt.encoding,
    enctype: elt.enctype,
    length: elt.length,
    method: elt.method,
    name: elt.name,
    noValidate: elt.noValidate,
    target: elt.target,
    rel: elt.rel,
  };
}

export function extractHTMLIFrameElement(elt: HTMLIFrameElement) {
  return {
    ...extractHTMLElementBase(elt),
    allow: elt.allow,
    allowFullscreen: elt.allowFullscreen,
    height: elt.height,
    name: elt.name,
    referrerPolicy: elt.referrerPolicy,
    src: elt.src,
    srcdoc: elt.srcdoc,
    width: elt.width,
    align: elt.align,
    frameBorder: elt.frameBorder,
    longDesc: elt.longDesc,
    marginHeight: elt.marginHeight,
    marginWidth: elt.marginWidth,
    scrolling: elt.scrolling,
    sandbox: elt.sandbox,
  };
}

export function extractHTMLImageElement(elt: HTMLImageElement) {
  return {
    ...extractHTMLElementBase(elt),
    alt: elt.alt,
    crossOrigin: elt.crossOrigin,
    decoding: elt.decoding,
    height: elt.height,
    isMap: elt.isMap,
    loading: elt.loading,
    naturalHeight: elt.naturalHeight,
    naturalWidth: elt.naturalWidth,
    referrerPolicy: elt.referrerPolicy,
    sizes: elt.sizes,
    src: elt.src,
    srcset: elt.srcset,
    useMap: elt.useMap,
    width: elt.width,
    align: elt.align,
    border: elt.border,
    complete: elt.complete,
    hspace: elt.hspace,
    longDesc: elt.longDesc,
    lowsrc: elt.lowsrc,
    name: elt.name,
    vspace: elt.vspace,
    x: elt.x,
    y: elt.y,
    fetchPriority: elt.fetchPriority,
  };
}

export function extractHTMLInputElement(elt: HTMLInputElement) {
  return {
    ...extractHTMLElementBase(elt),
    accept: elt.accept,
    alt: elt.alt,
    autocomplete: elt.autocomplete,
    checked: elt.checked,
    defaultChecked: elt.defaultChecked,
    defaultValue: elt.defaultValue,
    dirName: elt.dirName,
    disabled: elt.disabled,
    height: elt.height,
    indeterminate: elt.indeterminate,
    max: elt.max,
    maxLength: elt.maxLength,
    min: elt.min,
    minLength: elt.minLength,
    multiple: elt.multiple,
    name: elt.name,
    pattern: elt.pattern,
    placeholder: elt.placeholder,
    readOnly: elt.readOnly,
    required: elt.required,
    selectionDirection: elt.selectionDirection,
    selectionEnd: elt.selectionEnd,
    selectionStart: elt.selectionStart,
    size: elt.size,
    src: elt.src,
    step: elt.step,
    type: elt.type,
    value: elt.value,
    valueAsNumber: elt.valueAsNumber,
    width: elt.width,
    align: elt.align,
    capture: elt.capture,
    formAction: elt.formAction,
    formEnctype: elt.formEnctype,
    formMethod: elt.formMethod,
    formNoValidate: elt.formNoValidate,
    formTarget: elt.formTarget,
    useMap: elt.useMap,
    validationMessage: elt.validationMessage,
    willValidate: elt.willValidate,
    popoverTargetAction: elt.popoverTargetAction,
  };
}

export function extractHTMLLabelElement(elt: HTMLLabelElement) {
  return {
    ...extractHTMLElementBase(elt),
    htmlFor: elt.htmlFor,
  };
}

export function extractHTMLLiElement(elt: HTMLLIElement) {
  return {
    ...extractHTMLElementBase(elt),
    value: elt.value,
    type: elt.type,
  };
}

export function extractHTMLLinkElement(elt: HTMLLinkElement) {
  return {
    ...extractHTMLElementBase(elt),
    as: elt.as,
    crossOrigin: elt.crossOrigin,
    disabled: elt.disabled,
    fetchPriority: elt.fetchPriority,
    href: elt.href,
    hreflang: elt.hreflang,
    imageSizes: elt.imageSizes,
    imageSrcset: elt.imageSrcset,
    integrity: elt.integrity,
    media: elt.media,
    referrerPolicy: elt.referrerPolicy,
    rel: elt.rel,
    type: elt.type,
    charset: elt.charset,
    rev: elt.rev,
    target: elt.target,
    sizes: elt.sizes,
  };
}

export function extractHTMLMapElement(elt: HTMLMapElement) {
  return {
    ...extractHTMLElementBase(elt),
    name: elt.name,
  };
}

export function extractHTMLMeterElement(elt: HTMLMeterElement) {
  return {
    ...extractHTMLElementBase(elt),
    high: elt.high,
    low: elt.low,
    max: elt.max,
    min: elt.min,
    optimum: elt.optimum,
    value: elt.value,
  };
}

export function extractHTMLModElement(elt: HTMLModElement) {
  return {
    ...extractHTMLElementBase(elt),
    cite: elt.cite,
    dateTime: elt.dateTime,
  };
}

export function extractHTMLOListElement(elt: HTMLOListElement) {
  return {
    ...extractHTMLElementBase(elt),
    reversed: elt.reversed,
    start: elt.start,
    type: elt.type,
    compact: elt.compact,
  };
}

export function extractHTMLObjectElement(elt: HTMLObjectElement) {
  return {
    ...extractHTMLElementBase(elt),
    data: elt.data,
    height: elt.height,
    name: elt.name,
    type: elt.type,
    useMap: elt.useMap,
    width: elt.width,
    validationMessage: elt.validationMessage,
    willValidate: elt.willValidate,
    align: elt.align,
    archive: elt.archive,
    border: elt.border,
    code: elt.code,
    codeBase: elt.codeBase,
    codeType: elt.codeType,
    declare: elt.declare,
    hspace: elt.hspace,
    standby: elt.standby,
    vspace: elt.vspace,
  };
}

export function extractHTMLOptGroupElement(elt: HTMLOptGroupElement) {
  return {
    ...extractHTMLElementBase(elt),
    disabled: elt.disabled,
    label: elt.label,
  };
}

export function extractHTMLOptionElement(elt: HTMLOptionElement) {
  return {
    ...extractHTMLElementBase(elt),
    defaultSelected: elt.defaultSelected,
    disabled: elt.disabled,
    index: elt.index,
    label: elt.label,
    selected: elt.selected,
    text: elt.text,
    value: elt.value,
  };
}

export function extractHTMLOutputElement(elt: HTMLOutputElement) {
  return {
    ...extractHTMLElementBase(elt),
    defaultValue: elt.defaultValue,
    name: elt.name,
    type: elt.type,
    value: elt.value,
    htmlFor: elt.htmlFor,
    validationMessage: elt.validationMessage,
    willValidate: elt.willValidate,
  };
}

export function extractHTMLProgressElement(elt: HTMLProgressElement) {
  return {
    ...extractHTMLElementBase(elt),
    max: elt.max,
    position: elt.position,
    value: elt.value,
  };
}

export function extractHTMLQuoteElement(elt: HTMLQuoteElement) {
  return {
    ...extractHTMLElementBase(elt),
    cite: elt.cite,
  };
}

export function extractHTMLCiteElement(elt: HTMLElement) {
  return {
    ...extractHTMLElementBase(elt),
  };
}

export function extractHTMLScriptElement(elt: HTMLScriptElement) {
  return {
    ...extractHTMLElementBase(elt),
    async: elt.async,
    crossOrigin: elt.crossOrigin,
    defer: elt.defer,
    fetchPriority: elt.fetchPriority,
    integrity: elt.integrity,
    noModule: elt.noModule,
    referrerPolicy: elt.referrerPolicy,
    src: elt.src,
    text: elt.text,
    type: elt.type,
    charset: elt.charset,
  };
}

export function extractHTMLSelectElement(elt: HTMLSelectElement) {
  return {
    ...extractHTMLElementBase(elt),
    autocomplete: elt.autocomplete,
    disabled: elt.disabled,
    length: elt.length,
    multiple: elt.multiple,
    name: elt.name,
    required: elt.required,
    selectedIndex: elt.selectedIndex,
    size: elt.size,
    type: elt.type,
    value: elt.value,
    validationMessage: elt.validationMessage,
    willValidate: elt.willValidate,
  };
}

export function extractHTMLSlotElement(elt: HTMLSlotElement) {
  return {
    ...extractHTMLElementBase(elt),
    name: elt.name,
  };
}

export function extractHTMLSourceElement(elt: HTMLSourceElement) {
  return {
    ...extractHTMLElementBase(elt),
    height: elt.height,
    media: elt.media,
    sizes: elt.sizes,
    src: elt.src,
    srcset: elt.srcset,
    type: elt.type,
    width: elt.width,
  };
}

export function extractHTMLTableCaptionElement(elt: HTMLTableCaptionElement) {
  return {
    ...extractHTMLElementBase(elt),
    align: elt.align,
  };
}

export function extractHTMLTableCellElement(elt: HTMLTableCellElement) {
  return {
    ...extractHTMLElementBase(elt),
    abbr: elt.abbr,
    cellIndex: elt.cellIndex,
    colSpan: elt.colSpan,
    headers: elt.headers,
    rowSpan: elt.rowSpan,
    scope: elt.scope,
    align: elt.align,
    axis: elt.axis,
    bgColor: elt.bgColor,
    ch: elt.ch,
    chOff: elt.chOff,
    height: elt.height,
    noWrap: elt.noWrap,
    vAlign: elt.vAlign,
    width: elt.width,
  };
}

export function extractHTMLTableColElement(elt: HTMLTableColElement) {
  return {
    ...extractHTMLElementBase(elt),
    span: elt.span,
    align: elt.align,
    ch: elt.ch,
    chOff: elt.chOff,
    vAlign: elt.vAlign,
    width: elt.width,
  };
}

export function extractHTMLTableElement(elt: HTMLTableElement) {
  return {
    ...extractHTMLElementBase(elt),
    align: elt.align,
    bgColor: elt.bgColor,
    border: elt.border,
    cellPadding: elt.cellPadding,
    cellSpacing: elt.cellSpacing,
    frame: elt.frame,
    rules: elt.rules,
    summary: elt.summary,
    width: elt.width,
  };
}

export function extractHTMLTableRowElement(elt: HTMLTableRowElement) {
  return {
    ...extractHTMLElementBase(elt),
    rowIndex: elt.rowIndex,
    sectionRowIndex: elt.sectionRowIndex,
    align: elt.align,
    bgColor: elt.bgColor,
    ch: elt.ch,
    chOff: elt.chOff,
    vAlign: elt.vAlign,
  };
}

export function extractHTMLTableSectionElement(elt: HTMLTableSectionElement) {
  return {
    ...extractHTMLElementBase(elt),
    align: elt.align,
    ch: elt.ch,
    chOff: elt.chOff,
    vAlign: elt.vAlign,
  };
}

export function extractHTMLTemplateElement(elt: HTMLTemplateElement) {
  return {
    ...extractHTMLElementBase(elt),
  };
}

export function extractHTMLTextAreaElement(elt: HTMLTextAreaElement) {
  return {
    ...extractHTMLElementBase(elt),
    autocomplete: elt.autocomplete,
    cols: elt.cols,
    defaultValue: elt.defaultValue,
    dirName: elt.dirName,
    disabled: elt.disabled,
    maxLength: elt.maxLength,
    minLength: elt.minLength,
    name: elt.name,
    placeholder: elt.placeholder,
    readOnly: elt.readOnly,
    required: elt.required,
    rows: elt.rows,
    selectionDirection: elt.selectionDirection,
    selectionEnd: elt.selectionEnd,
    selectionStart: elt.selectionStart,
    value: elt.value,
    wrap: elt.wrap,
    textLength: elt.textLength,
    validationMessage: elt.validationMessage,
    willValidate: elt.willValidate,
  };
}

export function extractHTMLTimeElement(elt: HTMLTimeElement) {
  return {
    ...extractHTMLElementBase(elt),
    dateTime: elt.dateTime,
  };
}

export function extractHTMLTrackElement(elt: HTMLTrackElement) {
  return {
    ...extractHTMLElementBase(elt),
    default: elt.default,
    kind: elt.kind,
    label: elt.label,
    readyState: elt.readyState,
    src: elt.src,
    srclang: elt.srclang,
  };
}

export function extractHTMLVideoElement(elt: HTMLVideoElement) {
  return {
    ...extractHTMLMediaElement(elt),
    height: elt.height,
    poster: elt.poster,
    videoHeight: elt.videoHeight,
    videoWidth: elt.videoWidth,
    width: elt.width,
    playsInline: elt.playsInline,
  };
}

export function extractHTMLBRElement(elt: HTMLBRElement) {
  return {
    ...extractHTMLElementBase(elt),
    clear: elt.clear,
  };
}

export function extractHTMLBaseElement(elt: HTMLBaseElement) {
  return {
    ...extractHTMLElementBase(elt),
    href: elt.href,
    target: elt.target,
  };
}

export function extractHTMLBodyElement(elt: HTMLBodyElement) {
  return {
    ...extractHTMLElementBase(elt),
    aLink: elt.aLink,
    background: elt.background,
    bgColor: elt.bgColor,
    link: elt.link,
    text: elt.text,
    vLink: elt.vLink,
  };
}

export function extractHTMLDListElement(elt: HTMLDListElement) {
  return {
    ...extractHTMLElementBase(elt),
    compact: elt.compact,
  };
}

export function extractHTMLDetailsElement(elt: HTMLDetailsElement) {
  return {
    ...extractHTMLElementBase(elt),
    open: elt.open,
  };
}

export function extractHTMLDialogElement(elt: HTMLDialogElement) {
  return {
    ...extractHTMLElementBase(elt),
    open: elt.open,
    returnValue: elt.returnValue,
  };
}

export function extractHTMLDivElement(elt: HTMLDivElement) {
  return {
    ...extractHTMLElementBase(elt),
    align: elt.align,
  };
}

export function extractHTMLHeadElement(elt: HTMLHeadElement) {
  return {
    ...extractHTMLElementBase(elt),
  };
}

export function extractHTMLHeadingElement(elt: HTMLHeadingElement) {
  return {
    ...extractHTMLElementBase(elt),
    align: elt.align,
  };
}

export function extractHTMLHRElement(elt: HTMLHRElement) {
  return {
    ...extractHTMLElementBase(elt),
    align: elt.align,
    color: elt.color,
    noShade: elt.noShade,
    size: elt.size,
    width: elt.width,
  };
}

export function extractHTMLHtmlElement(elt: HTMLHtmlElement) {
  return {
    ...extractHTMLElementBase(elt),
    version: elt.version,
  };
}

export function extractHTMLMenuElement(elt: HTMLMenuElement) {
  return {
    ...extractHTMLElementBase(elt),
  };
}

export function extractHTMLMetaElement(elt: HTMLMetaElement) {
  return {
    ...extractHTMLElementBase(elt),
    content: elt.content,
    httpEquiv: elt.httpEquiv,
    name: elt.name,
    scheme: elt.scheme,
  };
}

export function extractHTMLParagraphElement(elt: HTMLParagraphElement) {
  return {
    ...extractHTMLElementBase(elt),
    align: elt.align,
  };
}

export function extractHTMLPictureElement(elt: HTMLPictureElement) {
  return {
    ...extractHTMLElementBase(elt),
  };
}

export function extractHTMLPreElement(elt: HTMLPreElement) {
  return {
    ...extractHTMLElementBase(elt),
    width: elt.width,
  };
}

export function extractHTMLSpanElement(elt: HTMLSpanElement) {
  return {
    ...extractHTMLElementBase(elt),
  };
}

export function extractHTMLStyleElement(elt: HTMLStyleElement) {
  return {
    ...extractHTMLElementBase(elt),
    media: elt.media,
    type: elt.type,
    disabled: elt.disabled,
  };
}

export function extractHTMLTitleElement(elt: HTMLTitleElement) {
  return {
    ...extractHTMLElementBase(elt),
    text: elt.text,
  };
}

export function extractHTMLUListElement(elt: HTMLUListElement) {
  return {
    ...extractHTMLElementBase(elt),
    compact: elt.compact,
    type: elt.type,
  };
}

export function extractHTMLElement(elt: HTMLElement): object {
  const tagName = elt.tagName.toUpperCase();

  switch (tagName) {
    case "A":
      return extractHTMLAnchorElement(elt as HTMLAnchorElement);
    case "AREA":
      return extractHTMLAreaElement(elt as HTMLAreaElement);
    case "AUDIO":
      return extractHTMLAudioElement(elt as HTMLAudioElement);
    case "BASE":
      return extractHTMLBaseElement(elt as HTMLBaseElement);
    case "BLOCKQUOTE":
    case "Q":
      return extractHTMLQuoteElement(elt as HTMLQuoteElement);
    case "BODY":
      return extractHTMLBodyElement(elt as HTMLBodyElement);
    case "BR":
      return extractHTMLBRElement(elt as HTMLBRElement);
    case "BUTTON":
      return extractHTMLButtonElement(elt as HTMLButtonElement);
    case "CANVAS": // Placeholder - no specific function yet
      return extractHTMLElementBase(elt);
    case "CAPTION":
      return extractHTMLTableCaptionElement(elt as HTMLTableCaptionElement);
    case "CITE":
      return extractHTMLCiteElement(elt); // Uses base HTMLElement
    case "COL":
    case "COLGROUP":
      return extractHTMLTableColElement(elt as HTMLTableColElement);
    case "DATA":
      return extractHTMLDataElement(elt as HTMLDataElement);
    case "DETAILS":
      return extractHTMLDetailsElement(elt as HTMLDetailsElement);
    case "DIALOG":
      return extractHTMLDialogElement(elt as HTMLDialogElement);
    case "DIV":
      return extractHTMLDivElement(elt as HTMLDivElement);
    case "DL":
      return extractHTMLDListElement(elt as HTMLDListElement);
    case "EMBED":
      return extractHTMLEmbedElement(elt as HTMLEmbedElement);
    case "FIELDSET":
      return extractHTMLFieldSetElement(elt as HTMLFieldSetElement);
    case "FORM":
      return extractHTMLFormElement(elt as HTMLFormElement);
    case "H1":
    case "H2":
    case "H3":
    case "H4":
    case "H5":
    case "H6":
      return extractHTMLHeadingElement(elt as HTMLHeadingElement);
    case "HEAD":
      return extractHTMLHeadElement(elt as HTMLHeadElement);
    case "HR":
      return extractHTMLHRElement(elt as HTMLHRElement);
    case "HTML":
      return extractHTMLHtmlElement(elt as HTMLHtmlElement);
    case "IFRAME":
      return extractHTMLIFrameElement(elt as HTMLIFrameElement);
    case "IMG":
      return extractHTMLImageElement(elt as HTMLImageElement);
    case "INPUT":
      return extractHTMLInputElement(elt as HTMLInputElement);
    case "LABEL":
      return extractHTMLLabelElement(elt as HTMLLabelElement);
    case "LI":
      return extractHTMLLiElement(elt as HTMLLIElement);
    case "LINK":
      return extractHTMLLinkElement(elt as HTMLLinkElement);
    case "MAP":
      return extractHTMLMapElement(elt as HTMLMapElement);
    case "MENU":
      return extractHTMLMenuElement(elt as HTMLMenuElement);
    case "META":
      return extractHTMLMetaElement(elt as HTMLMetaElement);
    case "METER":
      return extractHTMLMeterElement(elt as HTMLMeterElement);
    case "INS":
    case "DEL":
      return extractHTMLModElement(elt as HTMLModElement);
    case "OBJECT":
      return extractHTMLObjectElement(elt as HTMLObjectElement);
    case "OL":
      return extractHTMLOListElement(elt as HTMLOListElement);
    case "OPTGROUP":
      return extractHTMLOptGroupElement(elt as HTMLOptGroupElement);
    case "OPTION":
      return extractHTMLOptionElement(elt as HTMLOptionElement);
    case "OUTPUT":
      return extractHTMLOutputElement(elt as HTMLOutputElement);
    case "P":
      return extractHTMLParagraphElement(elt as HTMLParagraphElement);
    case "PICTURE":
      return extractHTMLPictureElement(elt as HTMLPictureElement);
    case "PRE":
      return extractHTMLPreElement(elt as HTMLPreElement);
    case "PROGRESS":
      return extractHTMLProgressElement(elt as HTMLProgressElement);
    case "SCRIPT":
      return extractHTMLScriptElement(elt as HTMLScriptElement);
    case "SELECT":
      return extractHTMLSelectElement(elt as HTMLSelectElement);
    case "SLOT":
      return extractHTMLSlotElement(elt as HTMLSlotElement);
    case "SOURCE":
      return extractHTMLSourceElement(elt as HTMLSourceElement);
    case "SPAN":
      return extractHTMLSpanElement(elt as HTMLSpanElement);
    case "STYLE":
      return extractHTMLStyleElement(elt as HTMLStyleElement);
    case "TABLE":
      return extractHTMLTableElement(elt as HTMLTableElement);
    case "TBODY":
    case "THEAD":
    case "TFOOT":
      return extractHTMLTableSectionElement(elt as HTMLTableSectionElement);
    case "TD":
    case "TH":
      return extractHTMLTableCellElement(elt as HTMLTableCellElement);
    case "TEMPLATE":
      return extractHTMLTemplateElement(elt as HTMLTemplateElement);
    case "TEXTAREA":
      return extractHTMLTextAreaElement(elt as HTMLTextAreaElement);
    case "TIME":
      return extractHTMLTimeElement(elt as HTMLTimeElement);
    case "TITLE":
      return extractHTMLTitleElement(elt as HTMLTitleElement);
    case "TR":
      return extractHTMLTableRowElement(elt as HTMLTableRowElement);
    case "TRACK":
      return extractHTMLTrackElement(elt as HTMLTrackElement);
    case "UL":
      return extractHTMLUListElement(elt as HTMLUListElement);
    case "VIDEO":
      return extractHTMLVideoElement(elt as HTMLVideoElement);
    // Add other tag names as needed
    default:
      throw new Error(
        `Unexpected HTML element tag: ${elt.tagName} (update .web/custom/serialize.ts)`
      );
  }
}

export function extractSyntheticEvent(evt: React.SyntheticEvent) {
  return {
    nativeEvent: cleanForSerialization(evt.nativeEvent),
    // use extractHTMLElement in every place where a HTMLElement or generic TElement type is used
    target: extractHTMLElement(evt.target as HTMLElement), // I think this is true for all or purposes
    // currentTarget is often not available in Reflex event handlers
    bubbles: evt.bubbles,
    cancelable: evt.cancelable,
    default_prevented: evt.defaultPrevented,
    event_phase: evt.eventPhase,
    is_trusted: evt.isTrusted,
    timestamp: evt.timeStamp,
    type: evt.type,
  };
}

export function extractUIEvent(evt: React.UIEvent) {
  return { ...extractSyntheticEvent(evt), detail: evt.detail };
}

export function extractMouseEvent(evt: React.MouseEvent) {
  return {
    ...extractUIEvent(evt),

    altKey: evt.altKey,
    button: evt.button,
    buttons: evt.buttons,
    clientX: evt.clientX,
    clientY: evt.clientY,
    ctrlKey: evt.ctrlKey,
    metaKey: evt.metaKey,
    movementX: evt.movementX,
    movementY: evt.movementY,
    pageX: evt.pageX,
    pageY: evt.pageY,
    relatedTarget: evt.relatedTarget
      ? extractHTMLElement(evt.relatedTarget as HTMLElement)
      : null,
    screenX: evt.screenX,
    screenY: evt.screenY,
    shiftKey: evt.shiftKey,
  };
}

export function extractClipboardEvent(evt: React.ClipboardEvent) {
  return {
    ...extractSyntheticEvent(evt),
    clipboard_data: evt.clipboardData,
  };
}

export function extractCompositionEvent(evt: React.CompositionEvent) {
  return {
    ...extractSyntheticEvent(evt),
    data: evt.data,
  };
}

export function extractDragEvent(evt: React.DragEvent) {
  return {
    ...extractMouseEvent(evt),
    data_transfer: evt.dataTransfer,
  };
}

export function extractPointerEvent(evt: React.PointerEvent) {
  return {
    ...extractMouseEvent(evt),
    pointer_id: evt.pointerId,
    pressure: evt.pressure,
    tangential_pressure: evt.tangentialPressure,
    tilt_x: evt.tiltX,
    tilt_y: evt.tiltY,
    twist: evt.twist,
    width: evt.width,
    height: evt.height,
    pointer_type: evt.pointerType,
    is_primary: evt.isPrimary,
  };
}

export function extractFocusEvent(evt: React.FocusEvent) {
  return {
    ...extractSyntheticEvent(evt),
    target: extractHTMLElement(evt.target as HTMLElement),
    related_target: evt.relatedTarget
      ? extractHTMLElement(evt.relatedTarget as HTMLElement)
      : null,
  };
}

export function extractFormEvent(evt: React.FormEvent) {
  return extractSyntheticEvent(evt);
}

export function extractInvalidEvent(evt: React.InvalidEvent) {
  return extractSyntheticEvent(evt)
}

export function extractChangeEvent(evt: React.ChangeEvent) {
  return extractFormEvent(evt);
}

export function extractKeyboardEvent(evt: React.KeyboardEvent) {
  return {
    ...extractUIEvent(evt),
    alt_key: evt.altKey,
    ctrl_key: evt.ctrlKey,
    code: evt.code,
    key: evt.key,
    locale: evt.locale,
    location: evt.location,
    meta_key: evt.metaKey,
    repeat: evt.repeat,
    shift_key: evt.shiftKey,
  };
}

export function extractTouchEvent(evt: React.TouchEvent) {
  return {
    ...extractUIEvent(evt),
    alt_key: evt.altKey,
    changed_touches: Array.from(evt.changedTouches).map((touch) => ({
      target: extractHTMLElement(touch.target as HTMLElement),
      identifier: touch.identifier,
      screen_x: touch.screenX,
      screen_y: touch.screenY,
      client_x: touch.clientX,
      client_y: touch.clientY,
      page_x: touch.pageX,
      page_y: touch.pageY,
    })),
    ctrl_key: evt.ctrlKey,
    meta_key: evt.metaKey,
    shift_key: evt.shiftKey,
    target_touches: Array.from(evt.targetTouches).map((touch) => ({
      target: extractHTMLElement(touch.target as HTMLElement),
      identifier: touch.identifier,
      screen_x: touch.screenX,
      screen_y: touch.screenY,
      client_x: touch.clientX,
      client_y: touch.clientY,
      page_x: touch.pageX,
      page_y: touch.pageY,
    })),
    touches: Array.from(evt.touches).map((touch) => ({
      target: extractHTMLElement(touch.target as HTMLElement),
      identifier: touch.identifier,
      screen_x: touch.screenX,
      screen_y: touch.screenY,
      client_x: touch.clientX,
      client_y: touch.clientY,
      page_x: touch.pageX,
      page_y: touch.pageY,
    })),
  };
}

export function extractWheelEvent(evt: React.WheelEvent) {
  return {
    ...extractMouseEvent(evt),
    delta_mode: evt.deltaMode,
    delta_x: evt.deltaX,
    delta_y: evt.deltaY,
    delta_z: evt.deltaZ,
  };
}

export function extractAnimationEvent(evt: React.AnimationEvent) {
  return {
    ...extractSyntheticEvent(evt),
    animation_name: evt.animationName,
    elapsed_time: evt.elapsedTime,
    pseudo_element: evt.pseudoElement,
  };
}

export function extractToggleEvent(evt: React.ToggleEvent) {
  return {
    ...extractSyntheticEvent(evt),
    old_state: evt.oldState,
    new_state: evt.newState,
  };
}

export function extractTransitionEvent(evt: React.TransitionEvent) {
  return {
    ...extractSyntheticEvent(evt),
    elapsed_time: evt.elapsedTime,
    property_name: evt.propertyName,
    pseudo_element: evt.pseudoElement,
  };
}
