from mangnify.ui.components.select_input_directory import (
    build_select_input_directory_button,
)


def init_ui(app):
    """
    Initialize the UI.
    """

    build_select_input_directory_button(app)

    app.main_box.add(app.select_input_directory_button)
