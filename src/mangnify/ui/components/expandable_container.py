import toga
from toga.style.pack import Pack, COLUMN


def build_expandable_container(app):
    """
    Build the expandable container.
    """

    app.expandable_container = toga.Box(style=Pack(direction=COLUMN))
