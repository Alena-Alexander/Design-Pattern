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


class TestVideoExporter(ABC):
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

    def prepare_export(self, audio_data):
        """
        Retrieves the actual audio data for WAV export(its layers, effects, and settings).

        :param audio_data:
        :return: File
        """
        print("Preparing audio data for WAV export")

    def do_export(self, folder: pathlib.Path):
        """
        Exports the data to a folder.

        :param folder:
        :return: File
        """
        print(f"Exporting audio data in WAV format to {folder}")


def main() -> None:
    """
    Main function.
    :return: None
    """

    # Asks for the preferred export quality
    export_quality: str # sets type as String
    while True:
        """
        As long as said while loop is true this program will ask the user to enter a desired quality for the export
        and if the quality is on of the option in "low", "high", "master" then the program will break, else it will dis-
        play a message saying "Unknown quality option: {export_quality}".
        """
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in {"low", "high", "master"}:
            break # Terminates the nearest enclosing loop and and skips the else clause if the loop has one
        else:
            print(f"Unknown quality option: {export_quality}")

    # Create the video and audio exporters, and executes depending on the quality the user chooses.
    """
    The program below executes two classes that will export audio and a video depending on the quality the user chooses.
    """
    video_exporter: VideoExporter
    audio_exporter: AudioExporter
    if export_quality == "low":
        video_exporter = H264BPVideoExporter()
        audio_exporter = ACCAudioExporter()
    elif export_quality == "high":
        video_exporter = H264Hi422PVideoExporter()
        audio_exporter = ACCAudioExporter()
    else:
        # The export quality is master.
        video_exporter = LosslessVideoExporter()
        audio_exporter = WAVAudioExporter()

    # Prepare the exports
    # This code retrieves data for the video and audio
    video_exporter.prepare_export("place_holder_for_audio_data")
    audio_exporter.prepare_export("place_holder_for_audio_data")

    # Do the export
    # assigns folder to a path to a file, and exports the video and audio to said file
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    main()
