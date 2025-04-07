from reflex_experiment.components.button import button
import reflex as rx

from reflex_experiment.elements import HTMLButtonElement
from reflex_experiment.events import MouseEvent


class State(rx.State):
    """The app state."""

    @rx.event
    def handle_evt(self, value: MouseEvent[HTMLButtonElement]):
        print(f"On click: {value} (type: {type(value)})")
        return None
