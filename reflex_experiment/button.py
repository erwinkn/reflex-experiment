import reflex as rx
from typing import Literal, Type, TypeVar, Unpack
from reflex_experiment.props import with_props
from reflex_experiment.attributes import ButtonHTMLAttributes
from reflex.vars import ObjectVar
from reflex.event import JavascriptInputEvent

class ButtonProps(ButtonHTMLAttributes, total=False):
    variant: Literal["default", "destructive", "outline", "secondary", "ghost", "link"]
    size: Literal["default", "sm", "lg", "icon"]
    as_child: bool


def input_event(e: ObjectVar[JavascriptInputEvent]) -> tuple[rx.Var[str]]:
    """Get the value from an input event.

    Args:
        e: The input event.

    Returns:
        The value from the input event.
    """
    print("E:",e)
    return (e.target.value,)

T = TypeVar("T", bound="rx.Component")

@with_props(ButtonProps)
class Button(rx.Component):
    """A button component based on shadcn/ui."""

    library = "$/custom/button"
    tag = "Button"

    test: rx.Var[str]
    

def button(*children, **kwargs: Unpack[ButtonProps]):
    return Button.create(*children, **kwargs)

__all__ = ["button", "Button"]
