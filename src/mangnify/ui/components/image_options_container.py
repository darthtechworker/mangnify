import toga
from toga.style.pack import Pack, COLUMN, ROW, BOLD

JPG_QUALITY_LABEL = "JPG Quality:"
TRIM_MARGINS_LABEL = "Trim Margins:"
TRIM_LIMIT_LABEL = "Trim Limit:"
ADD_MARGINS_LABEL = "Add Margins:"
ROTATE_SPREAD_LABEL = "Rotate Spread:"


def build_jpg_quality_container(app):
    """
    Build the JPG quality container.
    """

    app.jpg_quality_label = toga.Label(
        text=JPG_QUALITY_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 46, 0, 0)),
    )
    app.jpg_quality_dropdown = toga.Selection(
        items=[f"{i}%" for i in range(80, 101)],
        style=Pack(width=65),
        on_change=lambda widget: on_change_jpg_quality_dropdown(widget, app),
    )

    app.jpg_quality_container = toga.Box(
        style=Pack(direction=ROW, padding=(6, 102, 0, 102), height=31)
    )
    app.jpg_quality_container.add(app.jpg_quality_label)
    app.jpg_quality_container.add(app.jpg_quality_dropdown)


def on_change_jpg_quality_dropdown(widget, app):
    """
    Handle the select event on the JPG quality dropdown.
    """

    app.jpg_quality = int(widget.value[:-1])


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
        style=Pack(direction=ROW, padding=(0, 102, 0, 102), height=29)
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
        style=Pack(direction=ROW, padding=(0, 102, 0, 102), height=30)
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

    app.is_trim_images = widget.value

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
        style=Pack(direction=ROW, padding=(0, 102, 0, 102), height=29)
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
        text=ROTATE_SPREAD_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 54, 0, 0)),
    )
    app.rotate_spread_checkbox = toga.Switch(
        text="",
        on_change=lambda widget: on_change_rotate_spread_checkbox(widget, app),
    )

    app.rotate_spread_container = toga.Box(
        style=Pack(direction=ROW, padding=(0, 102, 0, 102))
    )
    app.rotate_spread_container.add(app.rotate_spread_label)
    app.rotate_spread_container.add(app.rotate_spread_checkbox)


def on_change_rotate_spread_checkbox(widget, app):
    """
    Handle the toggle event on the rotate spread checkbox.
    """

    app.is_rotate_spread = widget.value


def build_image_options_container(app):
    """
    Build the image options container.
    """

    build_jpg_quality_container(app)
    build_trim_margins_container(app)
    build_trim_margins_options_container(app)
    build_add_margins_container(app)
    build_rotate_spread_container(app)

    app.image_options_container = toga.Box(style=Pack(direction=COLUMN))
    app.image_options_container.add(app.jpg_quality_container)
    app.image_options_container.add(app.trim_margins_container)
    app.image_options_container.add(app.trim_margins_options_container)
    app.image_options_container.add(app.add_margins_container)
    app.image_options_container.add(app.rotate_spread_container)
