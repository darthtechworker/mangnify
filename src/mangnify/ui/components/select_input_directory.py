import asyncio

import toga
from toga.style.pack import BOLD, Pack

from mangnify.utils.comic_info import read_comic_info

SELECT_INPUT_DIRECTORY_LABEL = "Select Input Directory"


def build_select_input_directory_button(app):
    """
    Build the select input directory button.
    """

    app.select_input_directory_button = toga.Button(
        SELECT_INPUT_DIRECTORY_LABEL,
        on_press=lambda widget: asyncio.ensure_future(
            on_click_select_input_directory(widget, app)
        ),
        style=Pack(font_weight=BOLD, padding=(20, 80, 10, 80), height=30),
    )


async def on_click_select_input_directory(widget, app):
    """
    Handle the click event on the select input directory button.
    """

    dialog = toga.SelectFolderDialog(
        title=SELECT_INPUT_DIRECTORY_LABEL, initial_directory=None, multiple_select=None
    )
    selected_folder = await dialog._show(app.main_window)

    if selected_folder is not None:
        app.input_directory = selected_folder
        app.output_directory = app.input_directory / "output"
        app.working_directory = app.output_directory / ".tmp"
        read_comic_info(app)
