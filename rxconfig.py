import reflex as rx

config = rx.Config(
    app_name="reflex_experiment",
    tailwind={
        # We overwrite the `content`` configuration option to allow Tailwind to work with our custom components folder
        "content": [
            # These are the two default values
            "./pages/**/*.{js,ts,jsx,tsx}",
            "./utils/**/*.{js,ts,jsx,tsx}",
            # This one we add for our custom components
            "./custom/**/*.{js,ts,jsx,tsx}",
        ],
    },
)
