"""
main() uses dependency injection, it's getting a ready object and can get a custom factory object,
since it also uses dependency inversion by depending on abstract class.
"""

import pathlib
from abc import ABC, abstractmethod


class VideoExporter(ABC):
    @abstractmethod
    def prepare_export(self, video_data):
        pass

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        pass


class LosslessVideoExporter(VideoExporter):
    def prepare_export(self, video_data):
        pass

    def do_export(self, folder: pathlib.Path):
        pass


class H264BPVideoExporter(VideoExporter):
    def prepare_export(self, video_data):
        pass

    def do_export(self, folder: pathlib.Path):
        pass


class H264Hi422PVideoExporter(VideoExporter):
    def prepare_export(self, video_data):
        pass

    def do_export(self, folder: pathlib.Path):
        pass


class AudioExporter(ABC):
    @abstractmethod
    def prepare_export(self, audio_data):
        pass

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        pass


class AACAudioExporter(AudioExporter):
    def prepare_export(self, audio_data):
        pass

    def do_export(self, folder: pathlib.Path):
        pass


class WAVAudioExporter(AudioExporter):
    def prepare_export(self, audio_data):
        pass

    def do_export(self, folder: pathlib.Path):
        pass


class ExporterFactory(ABC):
    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        pass

    @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        pass


class FastExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class HighQualityExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class MasterQualityExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()


def read_exporter() -> ExporterFactory:
    factories = {
        "low": FastExporter,
        "high": HighQualityExporter,
        "master": MasterQualityExporter,
    }

    export_quality: str
    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unknown quality option: {export_quality}")


def main(fac: ExporterFactory) -> None:
    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()

    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == '__main__':
    factory = read_exporter()
    main(factory)
