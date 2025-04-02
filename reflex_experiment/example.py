from pydantic.v1 import BaseModel
from reflex.vars import ObjectVar, Var, ArrayVar

from reflex_experiment.elements import HTMLButtonElement
from reflex_experiment.events import MouseEvent, PointerEvent
from reflex_experiment.helpers import create_event_handler


class Value(BaseModel):
    value_test: float


# class PointerEvent(BaseModel):
#     """Interface for a Javascript PointerEvent."""

#     client_x: float
#     client_y: float
#     # screen_x: float
#     # screen_y: float
#     values_: list[Value]
#     single_value: Value


pointer_event = create_event_handler(MouseEvent, HTMLButtonElement)


# def map_value(value):
#     return {"value_test": value.to(ObjectVar).valueTest}
#
#
# def pointer_event(
#     e: ObjectVar,
# ) -> tuple[Var[PointerEvent]]:
#     """Get data from a pointer event as a single object.
#
#     Args:
#         e: The pointer event

#     Returns:
#         Tuple containing a single Var with the pointer event data
#     """
#     print("type of e.values:", type(e.values_.to(ArrayVar)))
#     return (
#         Var.create(
#             {
#                 "client_x": e.clientX,
#                 "client_y": e.clientY,
#                 "values_": e.values_.to(ArrayVar).foreach(map_value),
#                 "single_value": {"value_test": e.singleValue.to(ObjectVar).valueTest},
#                 # "xvalues_": rx.foreach(e.values, map_value),
#             }
#         ).to(PointerEvent),
#     )
