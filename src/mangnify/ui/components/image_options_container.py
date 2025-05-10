import toga
from toga.style.pack import BOLD, COLUMN, ROW, Pack

TRIM_MARGINS_LABEL = "Trim Margins:"
TRIM_LIMIT_LABEL = "Trim Limit:"
ADD_MARGINS_LABEL = "Add Margins:"
ROTATE_SPREADS_LABEL = "Rotate Spreads:"
SCALE_LABEL = "A.I. Upscale:"
SCALE_OPTIONS = ["None", "2x", "3x", "4x"]


def build_trim_margins_container(app):
    """
    Build the trim margins container.
    """

    app.trim_margins_label = toga.Label(
        text=TRIM_MARGINS_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 61, 0, 0)),
    )
    app.trim_margins_checkbox = toga.Switch(
        text="",
        on_change=lambda widget: on_change_trim_margins_checkbox(widget, app),
    )

    app.trim_margins_container = toga.Box(
        style=Pack(direction=ROW, padding=(0, 82, 0, 82), height=29)
    )
    app.trim_margins_container.add(app.trim_margins_label)
    app.trim_margins_container.add(app.trim_margins_checkbox)


def build_trim_limit_container(app):
    """
    Build the trim limit container.
    """

    app.trim_limit_label = toga.Label(
        text=TRIM_LIMIT_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 57, 0, 0)),
    )
    app.trim_limit_dropdown = toga.Selection(
        items=[f"{i}%" for i in range(10, 21)],
        style=Pack(width=65),
        on_change=lambda widget: on_change_trim_limit_dropdown(widget, app),
    )

    app.trim_limit_container = toga.Box(
        style=Pack(direction=ROW, padding=(0, 82, 0, 82), height=30)
    )
    app.trim_limit_container.add(app.trim_limit_label)
    app.trim_limit_container.add(app.trim_limit_dropdown)


def on_change_trim_limit_dropdown(widget, app):
    """
    Handle the select event on the trim limit dropdown.
    """

    app.trim_limit = int(widget.value[:-1])


def build_trim_margins_options_container(app):
    """
    Build the trim margins options container.
    """

    build_trim_limit_container(app)

    app.trim_margins_options_container = toga.Box(style=Pack(direction=COLUMN))


def on_change_trim_margins_checkbox(widget, app):
    """
    Handle the toggle event on the trim margins checkbox.
    """

    app.is_trim_margins = widget.value

    if widget.value:
        app.trim_margins_options_container.add(app.trim_limit_container)
    else:
        app.trim_margins_options_container.remove(app.trim_limit_container)

    app.resize_window()


def build_add_margins_container(app):
    """
    Build the add margins container.
    """

    app.add_margins_label = toga.Label(
        text=ADD_MARGINS_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 40, 0, 0)),
    )
    app.add_margins_dropdown = toga.Selection(
        items=[f"{i}%" for i in range(0, 11)],
        style=Pack(width=65),
        on_change=lambda widget: on_change_add_margins_dropdown(widget, app),
    )

    app.add_margins_container = toga.Box(
        style=Pack(direction=ROW, padding=(0, 82, 0, 82), height=30)
    )
    app.add_margins_container.add(app.add_margins_label)
    app.add_margins_container.add(app.add_margins_dropdown)


def on_change_add_margins_dropdown(widget, app):
    """
    Handle the select event on the add margins dropdown.
    """

    app.add_margins = int(widget.value[:-1])


def build_rotate_spread_container(app):
    """
    Build the rotate spread container.
    """

    app.rotate_spread_label = toga.Label(
        text=ROTATE_SPREADS_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 46, 0, 0)),
    )
    app.rotate_spread_checkbox = toga.Switch(
        text="",
        on_change=lambda widget: on_change_rotate_spread_checkbox(widget, app),
    )

    app.rotate_spread_container = toga.Box(
        style=Pack(direction=ROW, padding=(0, 82, 0, 82), height=29)
    )
    app.rotate_spread_container.add(app.rotate_spread_label)
    app.rotate_spread_container.add(app.rotate_spread_checkbox)


def on_change_rotate_spread_checkbox(widget, app):
    """
    Handle the toggle event on the rotate spread checkbox.
    """

    app.is_rotate_spread = widget.value


def build_scale_container(app):
    """
    Build the scale container.
    """

    app.scale_label = toga.Label(
        text=SCALE_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 44, 0, 0)),
    )
    app.scale_dropdown = toga.Selection(
        items=SCALE_OPTIONS,
        style=Pack(width=65),
        on_change=lambda widget: on_change_scale_dropdown(widget, app),
    )

    app.scale_container = toga.Box(style=Pack(direction=ROW, padding=(0, 82, 10, 82)))
    app.scale_container.add(app.scale_label)
    app.scale_container.add(app.scale_dropdown)


def on_change_scale_dropdown(widget, app):
    """
    Handle the select event on the scale dropdown.
    """

    app.scale_factor = int(widget.value[0]) if widget.value != "None" else None


def build_image_options_container(app):
    """
    Build the image options container.
    """

    build_trim_margins_container(app)
    build_trim_margins_options_container(app)
    build_add_margins_container(app)
    build_rotate_spread_container(app)
    build_scale_container(app)

    app.image_options_container = toga.Box(style=Pack(direction=COLUMN))
    app.image_options_container.add(app.trim_margins_container)
    app.image_options_container.add(app.trim_margins_options_container)
    app.image_options_container.add(app.add_margins_container)
    app.image_options_container.add(app.rotate_spread_container)
    app.image_options_container.add(app.scale_container)
