import toga
from toga.style.pack import Pack


def build_progress_bar(app):
    """
    Build the progress bar.
    """

    app.progress_bar = toga.ProgressBar(style=Pack(padding=(10, 40)), max=100)
