import reflex as rx
from typing import Sequence
from reflex.components.component import DEFAULT_TRIGGERS
from reflex.utils import types


class ComponentBase(rx.Component):
    def get_event_triggers(
        self,
    ) -> dict[str, types.ArgsSpec | Sequence[types.ArgsSpec]]:
        """Override to only return non-default triggers."""

        triggers = super().get_event_triggers()
        triggers = {k: v for k, v in triggers.items() if DEFAULT_TRIGGERS.get(k) != v}
        return triggers
