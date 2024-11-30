from mangnify.ui.components.select_input_directory import (
    build_select_input_directory_button,
)
from mangnify.ui.components.select_options_dropdown import (
    build_select_options_dropdown,
    OPTIONS,
)


def init_ui(app):
    """
    Initialize the UI.
    """

    build_select_input_directory_button(app)
    build_select_options_dropdown(app)

    app.main_box.add(app.select_input_directory_button)
    app.main_box.add(app.select_options_dropdown)

    app.select_options_dropdown.value = OPTIONS[0]
