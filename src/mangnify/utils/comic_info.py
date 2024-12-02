import os
import xml.etree.ElementTree as ET

from mangnify.ui.components.comic_info_options_container import on_change_manga_checkbox


def read_comic_info(app):
    """
    Read the comic info from the input directory and update the UI elements.
    """
    comic_info_path = os.path.join(app.input_directory, "ComicInfo.xml")

    if os.path.exists(comic_info_path):
        tree = ET.parse(comic_info_path)
        root = tree.getroot()

        title = root.find("Title").text if root.find("Title") is not None else ""
        series = root.find("Series").text if root.find("Series") is not None else ""
        volume = root.find("Volume").text if root.find("Volume") is not None else ""
        writer = root.find("Writer").text if root.find("Writer") is not None else ""
        manga = (
            root.find("Manga").text == "YesAndRightToLeft"
            if root.find("Manga") is not None
            else False
        )
    else:
        title = ""
        series = ""
        volume = ""
        writer = ""
        manga = False

    app.title_input.value = title
    app.series_input.value = series
    app.volume_input.value = volume
    app.writer_input.value = writer
    app.manga_checkbox.value = manga
    on_change_manga_checkbox(app.manga_checkbox, app)
