from my_config import Config
from mutagen.easyid3 import EasyID3 as mp3
from pathlib import Path, PurePath
import re


class Song(PurePath):
    def __init__(self, file:Path):
        # Behave as a Path object - allows file rename, etc
        super().__init__

        match self.suffix.upper():
            case ".MP3":
                self.metadata = mp3(file)

                self.title = self.metadata["title"][0]
                self.artists = self.metadata["artist"]
                self.album = self.metadata["album"]
                self.track = self.metadata["tracknumber"]
                self.genre = self.metadata["genre"]

            case _:
                print("Unsupported file type")


class Formatter:
    def keepNumbersOnly(self, inStr:str) -> str:
        return re.sub(r"\D+", "", inStr)

    def keepLettersAndNumbers(self, inStr:str) -> str:
        return re.sub("[^a-zA-Z0-9]", "", inStr)

config = Config()

