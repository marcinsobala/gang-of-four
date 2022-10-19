"""
main() function has low cohesion. It does too many different things. It has to know all types
of Audio and Video exporter which makes it coupled to all of them. It creates objects and uses
them. Usage should be separated from creation to enable provision of custom objects without
changing code.
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


def main() -> None:
    export_quality: str
    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in ("low", "high", "master"):
            break
        print(f"Unknown quality option: {export_quality}")

    video_exporter: VideoExporter
    audio_exporter: AudioExporter
    if export_quality == "low":
        video_exporter = H264BPVideoExporter()
        audio_exporter = AACAudioExporter()
    elif export_quality == "high":
        video_exporter = H264Hi422PVideoExporter()
        audio_exporter = AACAudioExporter()
    else:
        video_exporter = LosslessVideoExporter()
        audio_exporter = WAVAudioExporter()

    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)

if __name__ == '__main__':
    main()