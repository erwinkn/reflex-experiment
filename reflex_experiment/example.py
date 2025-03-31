from dataclasses import dataclass
from typing import TypedDict
from reflex.vars import Var, ObjectVar
from reflex.vars.base import VarData

@dataclass 
class PointerEvent:
    """Interface for a Javascript PointerEvent."""
    client_x: float = 0
    client_y: float = 0
    screen_x: float = 0
    screen_y: float = 0
    pressure: float = 0
    pointer_type: str = ""
    button: int = 0
    buttons: int = 0

class PointerEventDict(TypedDict):
    """Dict representation of pointer event data."""
    client_x: float
    client_y: float
    screen_x: float
    screen_y: float
    pressure: float
    pointer_type: str
    button: int 
    buttons: int

def pointer_event(e: ObjectVar[PointerEvent]) -> tuple[Var[PointerEventDict]]:
    """Get data from a pointer event as a single object.
    
    Args:
        e: The pointer event
        
    Returns:
        Tuple containing a single Var with the pointer event data
    """
    return (
        Var.create({
            "client_x": e.clientX,
            "client_y": e.clientY,
            "screen_x": e.screenX,
            "screen_y": e.screenY,
            "pressure": e.pressure,
            "pointer_type": e.pointerType,
            "button": e.button,
            "buttons": e.buttons
        }).to(PointerEventDict),
    )