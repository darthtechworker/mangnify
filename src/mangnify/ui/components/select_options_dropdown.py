import toga
from toga.style.pack import Pack

OPTIONS = [
    "1) Process Images",
    "2) Package into CBZ",
    "3) Process & package into CBZ",
    "4) Package into AZW3",
    "5) Process & package into AZW3",
]


def build_select_options_dropdown(app):
    """
    Build the select options dropdown.
    """

    app.select_options_dropdown = toga.Selection(
        items=OPTIONS,
        on_change=lambda widget: on_change_select_options_dropdown(widget, app),
        style=Pack(padding=(10, 60, 16, 60)),
    )


def on_change_select_options_dropdown(widget, app):
    """
    Handle the select event on the select options dropdown.
    """

    while len(app.dynamic_container.children):
        app.dynamic_container.remove(app.dynamic_container.children[0])

    update_comic_info_options_container(widget, app)

    selected_option = widget.value

    if selected_option == OPTIONS[0]:
        app.is_processing_needed = True
        app.is_cbz_needed = False
        app.is_azw3_needed = False

        app.dynamic_container.add(app.image_options_container)
        app.dynamic_container.add(app.output_options_container)

    if selected_option == OPTIONS[1]:
        app.is_processing_needed = False
        app.is_cbz_needed = True
        app.is_azw3_needed = False

        app.dynamic_container.add(app.comic_info_options_container)

    if selected_option == OPTIONS[2]:
        app.is_processing_needed = True
        app.is_cbz_needed = True
        app.is_azw3_needed = False

        app.dynamic_container.add(app.image_options_container)
        app.dynamic_container.add(app.output_options_container)
        app.dynamic_container.add(app.comic_info_options_container)

    if selected_option == OPTIONS[3]:
        app.is_processing_needed = False
        app.is_cbz_needed = False
        app.is_azw3_needed = True

        app.dynamic_container.add(app.comic_info_options_container)

    if selected_option == OPTIONS[4]:
        app.is_processing_needed = True
        app.is_cbz_needed = False
        app.is_azw3_needed = True

        app.dynamic_container.add(app.image_options_container)
        app.dynamic_container.add(app.output_options_container)
        app.dynamic_container.add(app.comic_info_options_container)

    app.resize_window()


def update_comic_info_options_container(widget, app):
    """
    Update the comic info options container.
    """

    while len(app.comic_info_options_container.children):
        app.comic_info_options_container.remove(
            app.comic_info_options_container.children[0]
        )

    app.comic_info_options_container.add(app.title_container)

    if widget.value in [OPTIONS[1], OPTIONS[2]]:
        app.comic_info_options_container.add(app.series_container)
        app.comic_info_options_container.add(app.volume_container)

    app.comic_info_options_container.add(app.writer_container)
    app.comic_info_options_container.add(app.manga_container)
