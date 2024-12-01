import toga
from toga.style.pack import Pack


def build_log_area(app):
    """
    Build the log area.
    """

    app.log_area = toga.MultilineTextInput(
        readonly=True,
        style=Pack(padding=(0, 20, 20, 20), height=150),
    )
    app.log_area.style.background_color = "lightgrey"
