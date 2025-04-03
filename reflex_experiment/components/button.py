import reflex as rx
from typing import Sequence
from reflex.event import EventHandler
from reflex.components.component import DEFAULT_TRIGGERS
from reflex.utils import types

from reflex_experiment.elements import HTMLButtonElement
from reflex_experiment.events import DOMEvents


class Base(rx.Component):
    def get_event_triggers(
        self,
    ) -> dict[str, types.ArgsSpec | Sequence[types.ArgsSpec]]:
        """Override to only return non-default triggers."""

        triggers = super().get_event_triggers()
        return {k: v for k, v in triggers.items() if DEFAULT_TRIGGERS.get(k) != v}

    def _exclude_props(self) -> list[str]:
        return [*super()._exclude_props(), "class_name"]


class Button(Base, DOMEvents(HTMLButtonElement)):
    """A button component based on shadcn/ui."""

    library = "$/custom/button"
    tag = "Button"


button = Button.create

__all__ = ["button", "Button"]
