import toga
from toga.style.pack import BOLD, COLUMN, ROW, Pack

TITLE = "Title:"
TITLE_PLACEHOLDER = "Manga|Comic Title (required)"
SERIES = "Series:"
SERIES_PLACEHOLDER = "Series Title (optional)"
VOLUME = "Volume:"
VOLUME_PLACEHOLDER = "Volume Number (optional)"
WRITER = "Writer:"
WRITER_PLACEHOLDER = "Writer Name (optional)"
MANGA = "Manga:"


def build_title_container(app):
    """
    Build the title container.
    """

    app.title_label = toga.Label(
        text=TITLE,
        style=Pack(font_weight=BOLD, flex=1),
    )

    app.title_input = toga.TextInput(
        style=Pack(flex=4),
        placeholder=TITLE_PLACEHOLDER,
        on_change=lambda widget: on_change_title_input(widget, app),
    )

    app.title_container = toga.Box(style=Pack(direction=ROW, padding=(2, 20, 8, 20)))
    app.title_container.add(app.title_label)
    app.title_container.add(app.title_input)


def on_change_title_input(widget, app):
    """
    Handle the change event on the title input.
    """

    app.title = widget.value


def build_series_container(app):
    """
    Build the series container.
    """

    app.series_label = toga.Label(
        text=SERIES,
        style=Pack(font_weight=BOLD, flex=1),
    )

    app.series_input = toga.TextInput(
        style=Pack(flex=4),
        placeholder=SERIES_PLACEHOLDER,
        on_change=lambda widget: on_change_series_input(widget, app),
    )

    app.series_container = toga.Box(style=Pack(direction=ROW, padding=(10, 20, 8, 20)))
    app.series_container.add(app.series_label)
    app.series_container.add(app.series_input)


def on_change_series_input(widget, app):
    """
    Handle the change event on the series input.
    """

    app.series = widget.value


def build_volume_container(app):
    """
    Build the volume container.
    """

    app.volume_label = toga.Label(
        text=VOLUME,
        style=Pack(font_weight=BOLD, flex=1),
    )

    app.volume_input = toga.TextInput(
        style=Pack(flex=4),
        placeholder=VOLUME_PLACEHOLDER,
        on_change=lambda widget: on_change_volume_input(widget, app),
    )

    app.volume_container = toga.Box(style=Pack(direction=ROW, padding=(10, 20, 8, 20)))
    app.volume_container.add(app.volume_label)
    app.volume_container.add(app.volume_input)


def on_change_volume_input(widget, app):
    """
    Handle the change event on the volume input.
    """

    app.volume = widget.value


def build_writer_container(app):
    """
    Build the writer container.
    """

    app.writer_label = toga.Label(
        text=WRITER,
        style=Pack(font_weight=BOLD, flex=1),
    )

    app.writer_input = toga.TextInput(
        style=Pack(flex=4),
        placeholder=WRITER_PLACEHOLDER,
        on_change=lambda widget: on_change_writer_input(widget, app),
    )

    app.writer_container = toga.Box(style=Pack(direction=ROW, padding=(10, 20, 15, 20)))
    app.writer_container.add(app.writer_label)
    app.writer_container.add(app.writer_input)


def on_change_writer_input(widget, app):
    """
    Handle the change event on the writer input.
    """

    app.writer = widget.value


def build_manga_container(app):
    """
    Build the manga container.
    """

    app.manga_label = toga.Label(
        text=MANGA,
        style=Pack(font_weight=BOLD, padding=(0, 102, 0, 0)),
    )
    app.manga_checkbox = toga.Switch(
        text="",
        on_change=lambda widget: on_change_manga_checkbox(widget, app),
    )

    app.manga_container = toga.Box(
        style=Pack(direction=ROW, padding=(0, 82, 0, 82), height=27)
    )
    app.manga_container.add(app.manga_label)
    app.manga_container.add(app.manga_checkbox)


def on_change_manga_checkbox(widget, app):
    """
    Handle the toggle event on the manga checkbox.
    """

    app.is_manga = widget.value


def build_comic_info_options_container(app):
    """
    Build the comic info options container.
    """

    build_title_container(app)
    build_series_container(app)
    build_volume_container(app)
    build_writer_container(app)
    build_manga_container(app)

    app.comic_info_options_container = toga.Box(style=Pack(direction=COLUMN))
