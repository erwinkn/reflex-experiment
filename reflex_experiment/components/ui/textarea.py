from reflex_experiment.attributes import HTMLTextareaProps


class Textarea(HTMLTextareaProps):
    """A textarea component based on shadcn/ui."""

    library = "$/custom/shadcn/textarea"
    tag = "Textarea"


textarea = Textarea.create


__all__ = ["textarea", "Textarea"]
