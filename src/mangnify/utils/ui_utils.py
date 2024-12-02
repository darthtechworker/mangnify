def toggle_ui(app, is_enabled):
    """
    Toggle the UI.
    """

    app.select_input_directory_button.enabled = is_enabled
    app.select_options_dropdown.enabled = is_enabled
    app.jpg_quality_dropdown.enabled = is_enabled
    app.trim_margins_checkbox.enabled = is_enabled
    app.trim_limit_dropdown.enabled = is_enabled
    app.add_margins_dropdown.enabled = is_enabled
    app.rotate_spread_checkbox.enabled = is_enabled
    app.scale_dropdown.enabled = is_enabled
    app.title_input.enabled = is_enabled
    app.series_input.enabled = is_enabled
    app.volume_input.enabled = is_enabled
    app.writer_input.enabled = is_enabled
    app.grayscale_checkbox.enabled = is_enabled
    app.compression_level_dropdown.enabled = is_enabled
    app.device_height_input.enabled = is_enabled
    app.device_width_input.enabled = is_enabled
    app.start_button.enabled = is_enabled
    app.abort_button.enabled = not is_enabled


def update_log_area(app, message):
    """
    Update the log area.
    """

    app.log_area.value += f"{message}\n"
    app.log_area.scroll_to_bottom()


def update_log_area_callback(app, message):
    """
    Update the log area callback
    """

    app.loop.call_later(0, update_log_area, app, message)


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