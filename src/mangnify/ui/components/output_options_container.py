import toga
from toga.style.pack import BOLD, COLUMN, ROW, Pack

GRAYSCALE_LABEL = "Grayscale:"
COMPRESSION_LEVEL_LABEL = "Compression:"
RESIZE_LABEL = "Resize:"
DEVICE_HEIGHT_LABEL = "Device Height:"
DEVICE_WIDTH_LABEL = "Device Width:"


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
        style=Pack(direction=ROW, padding=(0, 82, 0, 82), height=30)
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


def build_resize_container(app):
    """
    Build the resize container.
    """

    app.resize_label = toga.Label(
        text=RESIZE_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 103, 0, 0)),
    )
    app.resize_checkbox = toga.Switch(
        text="",
        on_change=lambda widget: on_change_resize_checkbox(widget, app),
    )

    app.resize_container = toga.Box(
        style=Pack(direction=ROW, padding=(0, 82, 0, 82), height=29)
    )
    app.resize_container.add(app.resize_label)
    app.resize_container.add(app.resize_checkbox)


def build_device_height_container(app):
    """
    Build the device height container.
    """

    app.device_height_label = toga.Label(
        text=DEVICE_HEIGHT_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 30, 0, 0)),
    )
    app.device_height_input = toga.TextInput(
        style=Pack(width=67),
        placeholder="px",
        on_change=lambda widget: on_change_device_height_input(widget, app),
    )

    app.device_height_container = toga.Box(
        style=Pack(direction=ROW, padding=(0, 82, 10, 82))
    )
    app.device_height_container.add(app.device_height_label)
    app.device_height_container.add(app.device_height_input)


def on_change_device_height_input(widget, app):
    """
    Handle the change event on the device height input.
    """

    widget.on_change = None
    widget.value = "".join(filter(str.isdigit, widget.value))
    app.device_height = int(widget.value) if widget.value else None
    widget.on_change = lambda widget: on_change_device_height_input(widget, app)


def build_device_width_container(app):
    """
    Build the device width container.
    """

    app.device_width_label = toga.Label(
        text=DEVICE_WIDTH_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 35, 0, 0)),
    )
    app.device_width_input = toga.TextInput(
        style=Pack(width=67),
        placeholder="px",
        on_change=lambda widget: on_change_device_width_input(widget, app),
    )

    app.device_width_container = toga.Box(
        style=Pack(direction=ROW, padding=(0, 82, 10, 82))
    )
    app.device_width_container.add(app.device_width_label)
    app.device_width_container.add(app.device_width_input)


def on_change_device_width_input(widget, app):
    """
    Handle the change event on the device width input.
    """

    widget.on_change = None
    widget.value = "".join(filter(str.isdigit, widget.value))
    app.device_width = int(widget.value) if widget.value else None
    widget.on_change = lambda widget: on_change_device_width_input(widget, app)


def build_device_dimensions_container(app):
    """
    Build the device dimensions container.
    """

    app.device_dimensions_container = toga.Box(style=Pack(direction=COLUMN))


def on_change_resize_checkbox(widget, app):
    """
    Handle the toggle event on the resize checkbox.
    """

    app.is_resize = widget.value

    if widget.value:
        app.device_dimensions_container.add(app.device_height_container)
        app.device_dimensions_container.add(app.device_width_container)
    else:
        app.device_dimensions_container.remove(app.device_height_container)
        app.device_dimensions_container.remove(app.device_width_container)

    app.resize_window()


def build_output_options_container(app):
    """
    Build the output options container.
    """

    build_grayscale_container(app)
    build_compression_level_container(app)
    build_resize_container(app)
    build_device_height_container(app)
    build_device_width_container(app)
    build_device_dimensions_container(app)

    app.output_options_container = toga.Box(style=Pack(direction=COLUMN))
    app.output_options_container.add(app.grayscale_container)
    app.output_options_container.add(app.compression_level_container)
    app.output_options_container.add(app.resize_container)
    app.output_options_container.add(app.device_dimensions_container)
