import googletrans
import reflex as rx


class Translation(rx.Base):
    original_text: str
    translated_text: str


class TranslationState(rx.State):
    input_text: str = "Hola Mundo"
    current_translation: Translation = Translation(original_text="", translated_text="")

    @rx.event
    def translate(self):
        self.current_translation.original_text = self.input_text
        self.current_translation.translated_text = (
            googletrans.Translator().translate(self.input_text, dest="en").text
        )


def translation_example():
    return rx.vstack(
        rx.input(
            on_change=lambda: [],
            on_blur=TranslationState.setvar("input_text"),
            default_value=TranslationState.input_text,
            placeholder="Text to translate...",
        ),
        rx.button("Translate", on_click=TranslationState.translate),
        rx.text(TranslationState.current_translation.translated_text),
    )
