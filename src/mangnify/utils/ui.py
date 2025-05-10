def toggle_ui(app, is_enabled):
    """
    Toggle the UI.
    """

    app.select_input_directory_button.enabled = is_enabled
    app.select_options_dropdown.enabled = is_enabled
    app.trim_margins_checkbox.enabled = is_enabled
    app.trim_limit_dropdown.enabled = is_enabled
    app.add_margins_dropdown.enabled = is_enabled
    app.rotate_spread_checkbox.enabled = is_enabled
    app.scale_dropdown.enabled = is_enabled
    app.title_input.enabled = is_enabled
    app.series_input.enabled = is_enabled
    app.volume_input.enabled = is_enabled
    app.writer_input.enabled = is_enabled
    app.manga_checkbox.enabled = is_enabled
    app.grayscale_checkbox.enabled = is_enabled
    app.compression_level_dropdown.enabled = is_enabled
    app.device_height_input.enabled = is_enabled
    app.device_width_input.enabled = is_enabled
    app.start_button.enabled = is_enabled
    app.abort_button.enabled = not is_enabled


def update_log_area(app, message, in_place=False):
    """
    Update the log area.
    """

    if in_place:
        lines = app.log_area.value.split("\n")
        if lines:
            lines[-1] = message
            app.log_area.value = "\n".join(lines)
        else:
            app.log_area.value = message
    else:
        app.log_area.value += f"{message}\n"

    app.log_area.scroll_to_bottom()


def update_log_area_callback(app, message, in_place=False):
    """
    Update the log area callback
    """

    app.loop.call_later(0, update_log_area, app, message, in_place)


def update_progress_bar(app, value):
    """
    Update the progress bar.
    """

    app.progress_bar.value = value


def update_progress_bar_callback(app, value):
    """
    Update the progress bar callback.
    """

    app.loop.call_later(0, update_progress_bar, app, value)


def is_valid_input(app):
    """
    Validate the input.
    """

    if not app.input_directory:
        update_log_area_callback(app, "Please select the input directory.")
        return False

    if app.is_resize:
        if not app.device_height_input.value:
            update_log_area_callback(app, "Please enter the device height.")
            return False

        if not app.device_width_input.value:
            update_log_area_callback(app, "Please enter the device width.")
            return False

    if app.is_cbz_needed or app.is_azw3_needed:
        if not app.title_input.value:
            update_log_area_callback(app, "Please enter the title.")
            return False

    return True
