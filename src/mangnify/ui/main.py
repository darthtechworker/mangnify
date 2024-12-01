from mangnify.ui.components.azw3_options_container import build_azw3_options_container
from mangnify.ui.components.comic_info_options_container import (
    build_comic_info_options_container,
)
from mangnify.ui.components.execution_buttons_container import (
    build_execution_buttons_container,
)
from mangnify.ui.components.image_options_container import build_image_options_container
from mangnify.ui.components.progress_bar import build_progress_bar
from mangnify.ui.components.select_input_directory import (
    build_select_input_directory_button,
)
from mangnify.ui.components.select_options_dropdown import (
    build_select_options_dropdown,
    OPTIONS,
)
from mangnify.ui.components.dynamic_container import build_dynamic_container


def build_ui(app):
    """
    Build the UI.
    """

    build_select_input_directory_button(app)
    build_select_options_dropdown(app)
    build_dynamic_container(app)
    build_image_options_container(app)
    build_comic_info_options_container(app)
    build_azw3_options_container(app)
    build_execution_buttons_container(app)
    build_progress_bar(app)

    app.main_box.add(app.select_input_directory_button)
    app.main_box.add(app.select_options_dropdown)
    app.main_box.add(app.dynamic_container)
    app.main_box.add(app.execution_buttons_container)
    app.main_box.add(app.progress_bar)

    init_ui(app)


def init_ui(app):
    """
    Initialize the UI.
    """

    app.select_options_dropdown.value = OPTIONS[0]

    app.jpg_quality_dropdown.value = "90%"
    app.trim_margins_checkbox.value = False
    app.trim_limit_dropdown.value = "10%"
    app.add_margins_dropdown.value = "0%"
    app.rotate_spread_checkbox.value = False

    # TODO: read and update comic info options from comic info file here

    app.abort_button.enabled = False

    app.progress_bar.value = 0
