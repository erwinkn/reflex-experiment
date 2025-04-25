import reflex as rx
from reflex_experiment.attributes import HTMLProps, HTMLInputProps, HTMLButtonProps
from reflex_experiment.helpers import TypedEventHandler


class CommandRoot(HTMLProps):
    """A command menu component based on shadcn/ui."""

    library = "$/custom/shadcn/command"
    tag = "Command"
    lib_dependencies = ["cmdk"]

    # Command specific props
    label: rx.Var[str]
    should_filter: rx.Var[bool]
    filter: TypedEventHandler[tuple[str, str, list[str] | None]]
    default_value: rx.Var[str]
    value: rx.Var[str]
    on_value_change: TypedEventHandler[str]
    loop: rx.Var[bool]
    disable_pointer_selection: rx.Var[bool]
    vim_bindings: rx.Var[bool]
    as_child: rx.Var[bool]


class CommandDialog(HTMLProps):
    """A dialog version of the command component."""

    library = "$/custom/shadcn/command"
    tag = "CommandDialog"

    # Dialog specific props
    default_open: rx.Var[bool]
    open: rx.Var[bool]
    on_open_change: TypedEventHandler[bool]
    modal: rx.Var[bool]


class CommandInput(HTMLInputProps):
    """An input for a command menu."""

    library = "$/custom/shadcn/command"
    tag = "CommandInput"

    as_child: rx.Var[bool]
    on_value_change: TypedEventHandler[str]


class CommandList(HTMLProps):
    """A list of command items."""

    library = "$/custom/shadcn/command"
    tag = "CommandList"

    as_child: rx.Var[bool]
    label: rx.Var[str]


class CommandEmpty(HTMLProps):
    """A component to display when no results are found."""

    library = "$/custom/shadcn/command"
    tag = "CommandEmpty"

    as_child: rx.Var[bool]


class CommandGroup(HTMLProps):
    """A group of command items."""

    library = "$/custom/shadcn/command"
    tag = "CommandGroup"

    # CommandGroup specific props
    heading: rx.Var[str]
    value: rx.Var[str]
    force_mount: rx.Var[bool]


class CommandItem(HTMLProps):
    """An item in a command menu."""

    library = "$/custom/shadcn/command"
    tag = "CommandItem"

    # CommandItem specific props
    disabled: rx.Var[bool]
    on_select: TypedEventHandler[str]
    value: rx.Var[str]
    keywords: rx.Var[list[str]]
    force_mount: rx.Var[bool]


class CommandSeparator(HTMLProps):
    """A separator between command items or groups."""

    library = "$/custom/shadcn/command"
    tag = "CommandSeparator"

    # CommandSeparator specific props
    always_render: rx.Var[bool]
    as_child: rx.Var[bool]


class CommandShortcut(HTMLProps):
    """A keyboard shortcut displayed in a command item."""

    library = "$/custom/shadcn/command"
    tag = "CommandShortcut"


class CommandNamespace(rx.ComponentNamespace):
    root = staticmethod(CommandRoot.create)
    dialog = staticmethod(CommandDialog.create)
    input = staticmethod(CommandInput.create)
    list = staticmethod(CommandList.create)
    empty = staticmethod(CommandEmpty.create)
    group = staticmethod(CommandGroup.create)
    item = staticmethod(CommandItem.create)
    separator = staticmethod(CommandSeparator.create)
    shortcut = staticmethod(CommandShortcut.create)


command = CommandNamespace()


__all__ = [
    "CommandRoot",
    "CommandDialog",
    "CommandInput",
    "CommandList",
    "CommandEmpty",
    "CommandGroup",
    "CommandItem",
    "CommandSeparator",
    "CommandShortcut",
    "command",
    "CommandNamespace",
]
