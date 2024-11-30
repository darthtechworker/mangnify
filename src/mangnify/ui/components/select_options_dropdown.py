import toga
from toga.style.pack import Pack

OPTIONS = [
    "1) Process Images",
    "2) Package into CBZ",
    "3) Process & package into CBZ",
    "4) Process & package into CBZ (keep files)",
    "5) Package into AZW3",
    "6) Process & package into AZW3",
    "7) Process & package into AZW3 (keep files)",
]


def build_select_options_dropdown(app):
    """
    Build the select options dropdown.
    """

    app.select_options_dropdown = toga.Selection(
        items=OPTIONS,
        on_change=lambda widget: on_change_select_options_dropdown(widget, app),
        style=Pack(padding=(10, 40, 10, 40)),
    )


def on_change_select_options_dropdown(widget, app):
    """
    Handle the select event on the select options dropdown.
    """

    selected_option = widget.value

    if selected_option == "1) Process Images":
        app.is_processing_needed = True
        app.is_keep_files = True

    if selected_option == "2) Package into CBZ":
        app.is_processing_needed = False
        app.is_keep_files = False

    if selected_option == "3) Process & package into CBZ":
        app.is_processing_needed = True
        app.is_keep_files = False

    if selected_option == "4) Process & package into CBZ (keep files)":
        app.is_processing_needed = True
        app.is_keep_files = True

    if selected_option == "5) Package into AZW3":
        app.is_processing_needed = False
        app.is_keep_files = False

    if selected_option == "6) Process & package into AZW3":
        app.is_processing_needed = True
        app.is_keep_files = False

    if selected_option == "7) Process & package into AZW3 (keep files)":
        app.is_processing_needed = True
        app.is_keep_files = True
