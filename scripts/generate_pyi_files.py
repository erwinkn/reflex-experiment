from reflex_experiment.pyi_generator import PyiGenerator
from pathlib import Path

# Assuming your custom components are in a directory called 'my_reflex_components'
# relative to where you run this script. Adjust the path as needed.
component_dirs = [Path(__file__).parent.parent / "reflex_experiment" / "components"]
component_dirs = [p.resolve() for p in component_dirs]

# Or specify individual files
# component_files = ["my_reflex_components/my_button.py"]

# --- Instantiate the generator ---
generator = PyiGenerator()

# --- Run the scan ---
# Pass the list of directories (or files) containing your components
generator.scan_all(targets=component_dirs)

print("Finished generating .pyi files.")
print("Generated files:", generator.written_files)
