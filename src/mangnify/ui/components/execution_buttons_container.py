import toga
from toga.style.pack import ROW, Pack

START_BUTTON_LABEL = "Start"
ABORT_BUTTON_LABEL = "Abort"


def build_execution_buttons_container(app):
    """
    Build the execution buttons container.
    """

    app.start_button = toga.Button(
        text=START_BUTTON_LABEL,
        on_press=lambda widget: on_press_start_button(widget, app),
        style=Pack(flex=1, height=30, padding=(0, 20), background_color="#0093E6"),
    )

    app.abort_button = toga.Button(
        text=ABORT_BUTTON_LABEL,
        on_press=lambda widget: on_press_abort_button(widget, app),
        style=Pack(flex=1, height=30, padding=(0, 20), background_color="#E65300"),
    )

    app.execution_buttons_container = toga.Box(
        style=Pack(direction=ROW, padding=(7, 40, 10, 40))
    )
    app.execution_buttons_container.add(app.start_button)
    app.execution_buttons_container.add(app.abort_button)


def on_press_start_button(widget, app):
    """
    Handle the press event on the start button.
    """

    pass


def on_press_abort_button(widget, app):
    """
    Handle the press event on the abort button.
    """

    pass
