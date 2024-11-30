from mangnify.ui.components.select_input_directory import (
    build_select_input_directory_button,
)
from mangnify.ui.components.select_options_dropdown import (
    build_select_options_dropdown,
    OPTIONS,
)
from mangnify.ui.components.expandable_container import build_expandable_container


def init_ui(app):
    """
    Initialize the UI.
    """

    build_select_input_directory_button(app)
    build_select_options_dropdown(app)
    build_expandable_container(app)

    app.main_box.add(app.select_input_directory_button)
    app.main_box.add(app.select_options_dropdown)
    app.main_box.add(app.expandable_container)

    app.select_options_dropdown.value = OPTIONS[0]
