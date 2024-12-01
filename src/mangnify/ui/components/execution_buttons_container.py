import toga
from toga.style.pack import ROW, Pack

from mangnify.utils import logging

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
    logger.info("Options Selected:")
    logger.info(f"Input Directory: {app.input_directory}")
    logger.info(f"Output Directory: {app.output_directory}")
    logger.info(f"Working Directory: {app.working_directory}")
    logger.info(f"Is Processing Needed: {app.is_processing_needed}")
    logger.info(f"Is Keep Images: {app.is_keep_images}")
    logger.info(f"JPG Quality: {app.jpg_quality}")
    logger.info(f"Is Trim Images: {app.is_trim_images}")
    logger.info(f"Trim Limit: {app.trim_limit}")
    logger.info(f"Add Margins: {app.add_margins}")
    logger.info(f"Is Rotate Spread: {app.is_rotate_spread}")
    logger.info(f"Scale Factor: {app.scale_factor}")
    logger.info(f"Is CBZ Needed: {app.is_cbz_needed}")
    logger.info(f"Is AZW3 Needed: {app.is_azw3_needed}")
    logger.info(f"Is Grayscale: {app.is_grayscale}")
    logger.info(f"Compression Level: {app.compression_level}")
    logger.info(f"Device Height: {app.device_height}")
    logger.info(f"Device Width: {app.device_width}")


def on_press_abort_button(widget, app):
    """
    Handle the press event on the abort button.
    """

    pass
