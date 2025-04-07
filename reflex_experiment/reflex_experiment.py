"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from reflex_experiment.components.button import button
from reflex_experiment.elements import HTMLButtonElement
from reflex_experiment.events import MouseEvent


class State(rx.State):
    """The app state."""

    @rx.event
    def handle_evt(self, value: MouseEvent[HTMLButtonElement]):
        print(f"On click: {value} (type: {type(value)})")
        return None


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            button("Click me!", class_name="bg-red-500", on_click=State.handle_evt),
            # rx.text(
            #     "Get started by editing ",
            #     rx.code(f"{config.app_name}/{config.app_name}.py"),
            #     size="5",
            # ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
