import reflex as rx
from reflex_experiment.attributes import HTMLProps, HTMLImgProps


class AvatarRoot(HTMLProps):
    """An avatar component based on shadcn/ui."""

    library = "$/custom/shadcn/avatar"
    tag = "Avatar"

    # Avatar specific props
    as_child: rx.Var[bool]


class AvatarImage(HTMLImgProps):
    """The image part of an avatar component."""

    library = "$/custom/shadcn/avatar"
    tag = "AvatarImage"

    as_child: rx.Var[bool]


class AvatarFallback(HTMLProps):
    """The fallback for an avatar component."""

    library = "$/custom/shadcn/avatar"
    tag = "AvatarFallback"

    # Fallback specific props
    as_child: rx.Var[bool]
    delay_ms: rx.Var[int]


class AvatarNamespace(rx.ComponentNamespace):
    root = staticmethod(AvatarRoot.create)
    image = staticmethod(AvatarImage.create)
    fallback = staticmethod(AvatarFallback.create)


avatar = AvatarNamespace()


__all__ = [
    "AvatarRoot",
    "AvatarImage",
    "AvatarFallback",
    "avatar",
    "AvatarNamespace",
]
