import toga
from toga.style.pack import BOLD, COLUMN, ROW, Pack

GRAYSCALE_LABEL = "Grayscale:"
COMPRESSION_LEVEL_LABEL = "Compression:"


def build_grayscale_container(app):
    """
    Build the grayscale container.
    """

    app.grayscale_label = toga.Label(
        text=GRAYSCALE_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 81, 0, 0)),
    )
    app.grayscale_checkbox = toga.Switch(
        text="",
        on_change=lambda widget: on_change_grayscale_checkbox(widget, app),
    )

    app.grayscale_container = toga.Box(
        style=Pack(direction=ROW, padding=(5, 82, 0, 82), height=30)
    )
    app.grayscale_container.add(app.grayscale_label)
    app.grayscale_container.add(app.grayscale_checkbox)


def on_change_grayscale_checkbox(widget, app):
    """
    Handle the toggle event on the grayscale checkbox.
    """

    app.is_grayscale = widget.value


def build_compression_level_container(app):
    """
    Build the compression level container.
    """

    app.compression_level_label = toga.Label(
        text=COMPRESSION_LEVEL_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 36, 0, 0)),
    )
    app.compression_level_dropdown = toga.Selection(
        items=[f"{i}%" for i in range(0, 26)],
        style=Pack(width=65),
        on_change=lambda widget: on_change_compression_level_dropdown(widget, app),
    )

    app.compression_level_container = toga.Box(
        style=Pack(direction=ROW, padding=(0, 82, 10, 82))
    )
    app.compression_level_container.add(app.compression_level_label)
    app.compression_level_container.add(app.compression_level_dropdown)


def on_change_compression_level_dropdown(widget, app):
    """
    Handle the change event on the compression level slider.
    """

    app.compression_level = int(widget.value[:-1])


def build_azw3_options_container(app):
    """
    Build the azw3 options container.
    """

    build_grayscale_container(app)
    build_compression_level_container(app)

    app.azw3_options_container = toga.Box(style=Pack(direction=COLUMN))
    app.azw3_options_container.add(app.grayscale_container)
    app.azw3_options_container.add(app.compression_level_container)
