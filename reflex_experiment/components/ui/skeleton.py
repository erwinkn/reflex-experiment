from reflex_experiment.attributes import HTMLProps


class Skeleton(HTMLProps):
    """A skeleton component based on shadcn/ui."""

    library = "$/custom/shadcn/skeleton"
    tag = "Skeleton"


skeleton = Skeleton.create


__all__ = ["skeleton", "Skeleton"]
