from mangnify.utils import logging
from mangnify.utils.file import (
    copy_images,
    create_directory,
    get_supported_images,
    package_azw3,
)
from mangnify.utils.image import load_image, resize_image, save_image
from mangnify.utils.ui import update_log_area_callback

logger = logging.getLogger(__name__)


def create_azw3(app) -> None:
    """
    Create the AZW3 file.
    """

    logger.info("Creating AZW3 file...")
    update_log_area_callback(app, "\nCreating AZW3 file...")

    try:
        create_directory(app.output_directory)
        create_directory(app.working_directory)

        if not app.is_processing_needed:
            copy_images(app.input_directory, app.working_directory)

        image_names = get_supported_images(app.working_directory)

        for image_name in image_names:
            if app.abort_event.is_set():
                raise Exception("Aborted by user.")

            image_path = app.working_directory / image_name
            image = load_image(image_path, app.is_grayscale)

            image = resize_image(image, app.device_height, app.device_width)

            save_image(image_path, image, 100)

        result = package_azw3(
            app.working_directory,
            app.output_directory,
            app.title,
            app.writer,
            app.is_manga,
            100 - app.compression_level,
        )

        update_log_area_callback(app, f"{result}")

    except Exception as e:
        logger.exception(e)
        raise e
