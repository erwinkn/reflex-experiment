from typing import Literal
import reflex as rx
from reflex_experiment.attributes import HTMLProps, HTMLButtonProps


        

def on_value_change(value: rx.Var) -> tuple[rx.Var[str]]:
    return (value,)


class AccordionRoot(HTMLProps):
    """An accordion component based on shadcn/ui."""

    library = "$/custom/shadcn/accordion"
    tag = "Accordion"

    as_child: rx.Var[bool]
    type: rx.Var[Literal["single", "multiple"]]
    default_value: rx.Var[str | list[str]]
    value: rx.Var[str | list[str]]
    on_value_change: rx.EventHandler[on_value_change]
    collapsible: rx.Var[bool]
    disabled: rx.Var[bool]
    # dir is a base HTML attribute
    orientation: rx.Var[Literal["vertical", "horizontal"]]


class AccordionItem(HTMLProps):
    """An item in an accordion component."""

    library = "$/custom/shadcn/accordion"
    tag = "AccordionItem"

    as_child: rx.Var[bool]
    disabled: rx.Var[bool]
    value: rx.Var[str]


class AccordionTrigger(HTMLButtonProps):
    """The trigger for an accordion item."""

    library = "$/custom/shadcn/accordion"
    tag = "AccordionTrigger"

    as_child: rx.Var[bool]


class AccordionContent(HTMLProps):
    """The content of an accordion item."""

    library = "$/custom/shadcn/accordion"
    tag = "AccordionContent"

    as_child: rx.Var[bool]
    force_mount: rx.Var[bool]


class AccordionNamespace(rx.ComponentNamespace):
    root = staticmethod(AccordionRoot.create)
    item = staticmethod(AccordionItem.create)
    trigger = staticmethod(AccordionTrigger.create)
    content = staticmethod(AccordionContent.create)


accordion = AccordionNamespace()

__all__ = [
    "AccordionRoot",
    "AccordionItem",
    "AccordionTrigger", 
    "AccordionContent",
    "accordion",
]

