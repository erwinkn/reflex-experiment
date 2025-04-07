from reflex_experiment.attributes import HTMLButtonProps


class Button(HTMLButtonProps):
    """A button component based on shadcn/ui."""

    library = "$/custom/shadcn/button"
    tag = "Button"


button = Button.create

__all__ = ["button", "Button"]
