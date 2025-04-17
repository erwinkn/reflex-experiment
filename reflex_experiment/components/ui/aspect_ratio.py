import reflex as rx
from reflex_experiment.attributes import HTMLProps


class AspectRatio(HTMLProps):
    """An aspect ratio component based on shadcn/ui."""

    library = "$/custom/shadcn/aspect-ratio"
    tag = "AspectRatio"

    # AspectRatio specific props
    ratio: rx.Var[float]
    as_child: rx.Var[bool]


aspect_ratio = AspectRatio.create


__all__ = ["aspect_ratio", "AspectRatio"]
