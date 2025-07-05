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
        :return: File
        """


class LosslessVideoExporter(VideoExporter):
    """
    Converts a video file containing its layers, effects, and settings, and exports after altering them, and uses the
    lossless format to export these changes into a playable video.
    """

    def prepare_export(self, video_data):
        """
        Retrieves the actual video data(its layers, effects, and settings) for exportation in the lossless format.

        :param video_data:
        :return: File
        """
        print("Preparing video data for lossless export.")

    def do_export(self, folder: pathlib.Path):
        """
        Exports the data to a folder in the lossless format.

        :param folder:
        :return: File
        """
        print(f"Exporting video data in a lossless format to {folder}")


class H264BPVideoExporter(VideoExporter):
    """
    Converts a video file containing its layers, effects, and settings, and exports after altering them, and uses the
    H.264 format with a Baseline profile(so low quality) to export these changes into a playable video.
    """

    def prepare_export(self, video_data):
        """
        Retrieves the actual video data(its layers, effects, and settings) for exportation in the H.264 format with a
        Baseline profile.

        :param video_data:
        :return: File
        """
        print("Preparing video data for H.264(Baseline) export.")

    def do_export(self, folder: pathlib.Path):
        """
        Exports the data to a folder in the lH.264 format with a Baseline profile.

        :param folder:
        :return: File
        """
        print(f"Exporting video data in a H.264(Baseline) format to {folder}")


class H264Hi422PVideoExporter(VideoExporter):
    """
    Converts a video file containing its layers, effects, and settings, and exports after altering them, and uses the
    H.264 format with a Hi422P Baseline profile(so high quality) to export these changes into a playable video.
    """

    def prepare_export(self, video_data):
        """
        Retrieves the actual video data(its layers, effects, and settings) for exportation in the H.264 format with a
        Hi422P profile.

        :param video_data:
        :return: File
        """
        print("Preparing video data for H.264(Hi422P) export.")

    def do_export(self, folder: pathlib.Path):
        """
        Exports the data to a folder in the H.264 format with a Hi422P profile.

        :param folder:
        :return: File
        """
        print(f"Exporting video data in a H.264(Hi422P) format to {folder}")


class AudioExporter(ABC):
    """
    Converts an audio file containing its layers, effects, and settings, and exports after altering them, and exports
    these changes into a playable audio file.
    """

    @abstractmethod
    def prepare_export(self, audio_data):
        """
        Retrieves the actual audio data(its layers, effects, and settings).

        :param audio_data:
        :return: File
        """

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """
        Exports the data to a folder.

        :param folder:
        :return: File
        """


class ACCAudioExporter(AudioExporter):
    """
    Converts an audio file containing its layers, effects, and settings, and exports after altering them, and exports
    these changes in the ACC format into a playable audio file.
    """

    def prepare_export(self, audio_data):
        """
        Retrieves the actual audio data for ACC export(its layers, effects, and settings).

        :param audio_data:
        :return: File
        """
        print("Preparing audio data for ACC export")

    def do_export(self, folder: pathlib.Path):
        """
        Exports the data to a folder.

        :param folder:
        :return: File
        """
        print(f"Exporting audio data in ACC format to {folder}")

class WAVAudioExporter(AudioExporter):
    """
    Converts an audio file containing its layers, effects, and settings, and exports after altering them, and exports
    these changes in the WAV format into a playable audio file.
    """


