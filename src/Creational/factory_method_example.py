"""
Basic video exporting example

Exporting means converting a project into a playable video file, which typically involves compressing and encoding a
video, making it ready to shared.

From project to file:
A video project, includes its layers, effects, and settings, its initially saved as a project file. Exporting changes
this file into a single, playable video file
"""

import pathlib
from abc import ABC, abstractmethod


class VideoExporter(ABC):
    """
    An abstract class that contains two methods that only describes how other classes should implement them
    and the functions of a Video exporter.

    Converts a video file containing its layers, effects, and settings, and exports after altering them, and exports
    these changes into a playable video.
    """

    @abstractmethod
    def prepare_export(self, video_data):
        """
        Retrieves the actual video data(its layers, effects, and settings).

        :param video_data:
        :return: File
        """

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """
        Exports the data to a folder.

        :param folder:
        :return:
        """

class LosslessVideoExporter(VideoExporter):
    """
    Converts a video file containing its layers, effects, and settings, and exports after altering them, and exports
    these changes into a playable video.
    """
    def prepare_export(self, video_data):


    def do_export(self, folder: pathlib.Path):

class LosslessVideoExporter(VideoExporter):
    """

    """

    def prepare_export(self, video_data):

    def do_export(self, folder: pathlib.Path):


