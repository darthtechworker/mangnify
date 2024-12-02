import threading

import toga
from toga.style.pack import ROW, Pack

from mangnify.create_azw3 import create_azw3
from mangnify.create_cbz import create_cbz
from mangnify.process_images import process_images
from mangnify.utils import logging
from mangnify.utils.ui import is_valid_input, toggle_ui, update_log_area_callback

START_BUTTON_LABEL = "Start"
ABORT_BUTTON_LABEL = "Abort"

logger = logging.getLogger(__name__)


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

    options_selected = (
        f"\n\n\nOptions Selected:\n\n"
        f"Input Directory:      {app.input_directory}\n"
        f"Output Directory:     {app.output_directory}\n"
        f"Working Directory:    {app.working_directory}\n"
        f"Is Processing Needed: {app.is_processing_needed}\n"
        f"Is Keep Images:       {app.is_keep_images}\n"
        f"JPG Quality:          {app.jpg_quality}\n"
        f"Is Trim Margins:      {app.is_trim_margins}\n"
        f"Trim Limit:           {app.trim_limit}\n"
        f"Add Margins:          {app.add_margins}\n"
        f"Is Rotate Spread:     {app.is_rotate_spread}\n"
        f"Scale Factor:         {app.scale_factor}\n"
        f"Is CBZ Needed:        {app.is_cbz_needed}\n"
        f"Is AZW3 Needed:       {app.is_azw3_needed}\n"
        f"Is Grayscale:         {app.is_grayscale}\n"
        f"Compression Level:    {app.compression_level}\n"
        f"Device Height:        {app.device_height}\n"
        f"Device Width:         {app.device_width}\n\n\n"
    )
    logger.info(options_selected)

    if is_valid_input(app):

        app.abort_event.clear()
        toggle_ui(app, False)
        app.progress_bar.value = 0
        app.log_area.value = ""

        def task():

            try:
                update_log_area_callback(app, "Mangnifying...")

                if app.is_processing_needed:
                    process_images(app)

                if app.is_cbz_needed:
                    create_cbz(app)

                if app.is_azw3_needed:
                    create_azw3(app)

                update_log_area_callback(app, "\nMangnification completed.")

            except Exception as e:
                logger.error(e)
                update_log_area_callback(app, f"\n{e}")

            finally:
                toggle_ui(app, True)

        threading.Thread(target=task).start()


def on_press_abort_button(widget, app):
    """
    Handle the press event on the abort button.
    """

    app.abort_event.set()
