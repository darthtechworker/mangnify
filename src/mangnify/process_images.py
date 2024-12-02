from mangnify.utils import logging
from mangnify.utils.file_utils import create_directory, get_supported_images
from mangnify.utils.image_utils import load_image, save_image, trim_margins
from mangnify.utils.ui_utils import (
    update_log_area_callback,
    update_progress_bar_callback,
)

logger = logging.getLogger(__name__)


def process_images(app) -> None:
    """
    Process the images.
    """

    logger.info("Processing images...")
    update_log_area_callback(app, "\nProcessing images...")

    try:
        create_directory(app.output_directory)
        create_directory(app.working_directory)

        image_names = get_supported_images(app.input_directory)

        total_images = len(image_names)
        current_image_count = 0
        original_size = 0
        processed_size = 0

        for image_name in image_names:
            if app.abort_event.is_set():
                raise Exception("Aborted by user.")

            image_path = app.input_directory / image_name
            image = load_image(image_path)

            original_size += image_path.stat().st_size

            if app.is_trim_margins:
                image = trim_margins(image, app.trim_limit)

            new_image_name = image_name.split(".")[0] + "_mangnified.jpg"
            new_image_path = app.working_directory / new_image_name
            save_image(new_image_path, image, app.jpg_quality)

            processed_size += new_image_path.stat().st_size

            current_image_count += 1
            progress = (current_image_count / total_images) * 100
            update_progress_bar_callback(app, progress)

    except Exception as e:
        logger.exception(e)
        raise e

    logger.info("Images processed.")
    original_size_mb = original_size / (1024 * 1024)
    processed_size_mb = processed_size / (1024 * 1024)
    update_log_area_callback(
        app,
        f"Images processed.\n\nOriginal Size: {original_size_mb:.2f} MB\nProcessed Size: {processed_size_mb:.2f} MB",
    )
