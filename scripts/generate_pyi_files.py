from reflex_experiment.pyi_generator import PyiGenerator, DEFAULT_IMPORTS
from pathlib import Path

# Assuming your custom components are in a directory called 'my_reflex_components'
# relative to where you run this script. Adjust the path as needed.
component_dirs = [Path(__file__).parent.parent / "reflex_experiment" / "components"]

# Or specify individual files
# component_files = ["my_reflex_components/my_button.py"]

# --- Instantiate the generator ---
DEFAULT_IMPORTS["reflex_experiment.events"] = [
    "SyntheticEvent",
    "UIEvent",
    "ClipboardEvent",
    "CompositionEvent",
    "DragEvent",
    "PointerEvent",
    "FocusEvent",
    "FormEvent",
    "KeyboardEvent",
    "MouseEvent",
    "TouchEvent",
    "WheelEvent",
    "AnimationEvent",
    "ToggleEvent",
    "TransitionEvent",
    "ChangeEvent",
    "DOMEvents",
]
generator = PyiGenerator()

# --- Run the scan ---
# Pass the list of directories (or files) containing your components
generator.scan_all(targets=component_dirs)

print("Finished generating .pyi files.")
print("Generated files:", generator.written_files)
