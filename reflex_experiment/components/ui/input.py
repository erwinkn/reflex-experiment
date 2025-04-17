from reflex_experiment.attributes import HTMLInputProps


class Input(HTMLInputProps):
    """An input component based on shadcn/ui."""

    library = "$/custom/shadcn/input"
    tag = "Input"


input = Input.create


__all__ = ["input", "Input"]
