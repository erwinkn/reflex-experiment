from typing import Callable, Literal, Unpack
import reflex as rx
from .attributes import ButtonHTMLAttributes, HTMLAttributes
from .props import with_props


class AccordionProps(HTMLAttributes, total=False):
    as_child: bool
    type: Literal["single", "multiple"]
    default_value: str | list[str]
    value: str | list[str]
    on_value_change: Callable[[str], None]
    collapsible: bool
    disabled: bool
    # dir is a base HTML attribute
    orientation: Literal["vertical", "horizontal"]


@with_props(AccordionProps)
class AccordionRoot(rx.Component):
    """An accordion component based on shadcn/ui."""

    library = "$/custom/shadcn/accordion"
    tag = "Accordion"
    lib_dependencies = [
        "clsx",
        "tailwind-merge",
        "@radix-ui/react-accordion",
        "lucide-react",
    ]

    @classmethod
    def create(cls, *args, **kwargs: Unpack[AccordionProps]):
        return super().create(*args, **kwargs)


class AccordionItemProps(HTMLAttributes, total=False):
    as_child: bool
    disabled: bool
    value: str


@with_props(AccordionItemProps)
class AccordionItem(rx.Component):
    """An item in an accordion component."""

    library = "$/custom/shadcn/accordion"
    tag = "AccordionItem"

    @classmethod
    def create(cls, *args, **kwargs: Unpack[AccordionItemProps]):
        return super().create(*args, **kwargs)


class AccordionTriggerProps(ButtonHTMLAttributes, total=False):
    as_child: bool


@with_props(AccordionTriggerProps)
class AccordionTrigger(rx.Component):
    """The trigger for an accordion item."""

    library = "$/custom/shadcn/accordion"
    tag = "AccordionTrigger"

    @classmethod
    def create(cls, *args, **kwargs: Unpack[AccordionTriggerProps]):
        return super().create(*args, **kwargs)


class AccordionContentProps(HTMLAttributes, total=False):
    as_child: bool
    force_mount: bool


@with_props(AccordionContentProps)
class AccordionContent(rx.Component):
    """The content of an accordion item."""

    library = "$/custom/shadcn/accordion"
    tag = "AccordionContent"

    @classmethod
    def create(cls, *args, **kwargs: Unpack[AccordionContentProps]):
        return super().create(*args, **kwargs)


class AccordionNamespace(rx.ComponentNamespace):
    root = staticmethod(AccordionRoot.create)
    item = staticmethod(AccordionItem.create)
    trigger = staticmethod(AccordionTrigger.create)
    content = staticmethod(AccordionContent.create)


accordion = AccordionNamespace()
