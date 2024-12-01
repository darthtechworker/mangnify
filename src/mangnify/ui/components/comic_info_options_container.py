import toga
from toga.style.pack import Pack, COLUMN, ROW, BOLD

TITLE = "Title:"
TITLE_PLACEHOLDER = "Manga|Comic Title (required)"
SERIES = "Series:"
SERIES_PLACEHOLDER = "Series Title (optional)"
VOLUME = "Volume:"
VOLUME_PLACEHOLDER = "Volume Number (optional)"
WRITER = "Writer:"
WRITER_PLACEHOLDER = "Writer Name (optional)"


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
    )

    app.title_container = toga.Box(style=Pack(direction=ROW, padding=(16, 40, 8, 40)))
    app.title_container.add(app.title_label)
    app.title_container.add(app.title_input)


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
    )

    app.series_container = toga.Box(style=Pack(direction=ROW, padding=(10, 40, 8, 40)))
    app.series_container.add(app.series_label)
    app.series_container.add(app.series_input)


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
    )

    app.volume_container = toga.Box(style=Pack(direction=ROW, padding=(10, 40, 8, 40)))
    app.volume_container.add(app.volume_label)
    app.volume_container.add(app.volume_input)


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
    )

    app.writer_container = toga.Box(style=Pack(direction=ROW, padding=(10, 40, 8, 40)))
    app.writer_container.add(app.writer_label)
    app.writer_container.add(app.writer_input)


def build_comic_info_options_container(app):
    """
    Build the comic info options container.
    """

    build_title_container(app)
    build_series_container(app)
    build_volume_container(app)
    build_writer_container(app)

    app.comic_info_options_container = toga.Box(style=Pack(direction=COLUMN))
