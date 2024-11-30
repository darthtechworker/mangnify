import toga
from toga.style.pack import Pack, COLUMN


def build_dynamic_container(app):
    """
    Build the dynamic container.
    """

    app.dynamic_container = toga.Box(style=Pack(direction=COLUMN))
