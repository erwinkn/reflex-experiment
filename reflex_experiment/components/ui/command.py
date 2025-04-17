import reflex as rx
from stoneware_app.components.helpers.styling import apply_tailwind_styles
from stoneware_app.components.ui.dialog import DialogAttributes
from ..attributes import HTMLAttributes, InputHTMLAttributes


class Command(rx.Component, HTMLAttributes):
    """A command menu component based on shadcn/ui."""

    library = "$/custom/shadcn/command"
    tag = "Command"
    lib_dependencies = ["cmdk"]

    # Command specific props
    label: rx.Var[str]
    should_filter: rx.Var[bool]
    filter: rx.EventHandler[lambda value, search, keywords: [value, search, keywords]]
    default_value: rx.Var[str]
    value: rx.Var[str]
    on_value_change: rx.EventHandler[lambda value: [value]]
    loop: rx.Var[bool]
    disable_pointer_selection: rx.Var[bool]
    vim_bindings: rx.Var[bool]
    as_child: rx.Var[bool]


class CommandDialog(rx.Component, DialogAttributes):
    library = "$/custom/shadcn/command"
    tag = "CommandDialog"


class CommandInput(rx.Component, InputHTMLAttributes):
    """An input for a command menu."""

    library = "$/custom/shadcn/command"
    tag = "CommandInput"

    as_child: rx.Var[bool]
    on_value_change: rx.EventHandler[lambda search: [search]]


class CommandList(rx.Component, HTMLAttributes):
    """A list of command items."""

    library = "$/custom/shadcn/command"
    tag = "CommandList"

    as_child: rx.Var[bool]
    label: rx.Var[str]


class CommandEmpty(rx.Component, HTMLAttributes):
    """A component to display when no results are found."""

    library = "$/custom/shadcn/command"
    tag = "CommandEmpty"

    as_child: rx.Var[bool]


class CommandGroup(rx.Component, HTMLAttributes):
    """A group of command items."""

    library = "$/custom/shadcn/command"
    tag = "CommandGroup"

    # CommandGroup specific props
    heading: rx.Var[str]
    value: rx.Var[str]
    force_mount: rx.Var[bool]


class CommandItem(rx.Component, HTMLAttributes):
    """An item in a command menu."""

    library = "$/custom/shadcn/command"
    tag = "CommandItem"

    # CommandItem specific props
    disabled: rx.Var[bool] = rx.Var.create(False)
    on_select: rx.EventHandler[lambda value: [value]]
    value: rx.Var[str]
    keywords: rx.Var[list[str]]
    force_mount: rx.Var[bool]


class CommandSeparator(rx.Component, HTMLAttributes):
    """A separator between command items or groups."""

    library = "$/custom/shadcn/command"
    tag = "CommandSeparator"

    # CommandSeparator specific props
    always_render: rx.Var[bool]
    as_child: rx.Var[bool]


class CommandShortcut(rx.Component, HTMLAttributes):
    """A keyboard shortcut displayed in a command item."""

    library = "$/custom/shadcn/command"
    tag = "CommandShortcut"


# Create helper functions
def command(*children, **props):
    """Create a Command component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return Command.create(*children, **updated_props)


def command_input(*children, **props):
    """Create a CommandInput component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return CommandInput.create(*children, **updated_props)


def command_list(*children, **props):
    """Create a CommandList component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return CommandList.create(*children, **updated_props)


def command_empty(*children, **props):
    """Create a CommandEmpty component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return CommandEmpty.create(*children, **updated_props)


def command_group(*children, **props):
    """Create a CommandGroup component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return CommandGroup.create(*children, **updated_props)


def command_item(*children, **props):
    """Create a CommandItem component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return CommandItem.create(*children, **updated_props)


def command_separator(*children, **props):
    """Create a CommandSeparator component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return CommandSeparator.create(*children, **updated_props)


def command_shortcut(*children, **props):
    """Create a CommandShortcut component with styling support."""
    # Apply Tailwind styles from props
    updated_props = apply_tailwind_styles(**props)
    return CommandShortcut.create(*children, **updated_props)


__all__ = [
    "Command",
    "command",
    "CommandInput",
    "command_input",
    "CommandList",
    "command_list",
    "CommandEmpty",
    "command_empty",
    "CommandGroup",
    "command_group",
    "CommandItem",
    "command_item",
    "CommandSeparator",
    "command_separator",
    "CommandShortcut",
    "command_shortcut",
]
