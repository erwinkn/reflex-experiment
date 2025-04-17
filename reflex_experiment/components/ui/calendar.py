import reflex as rx
from reflex_experiment.attributes import HTMLProps


class Calendar(HTMLProps):
    """A calendar component based on shadcn/ui."""

    library = "$/custom/shadcn/calendar"
    tag = "Calendar"
    lib_dependencies = ["react-day-picker@8.10.1", "date-fns"]

    # Calendar specific props
    class_names: rx.Var[dict[str, str]]
    show_outside_days: rx.Var[bool]
    # Add more as needed


calendar = Calendar.create


__all__ = ["calendar", "Calendar"]
