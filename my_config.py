from pathlib import Path
import json

DEFAULT_STATE = {
    "prefixes": {
        "track_no": "00",
        "album_year": "[0000]"
    },
    "formatting": {
        "lower_case": [
            "of",
            "is",
            "and",
            "the",
            "to",
            "for"
        ]
    }
}
CONFIG_DIR = Path(Path.home(), ".irmomelian")

class Config:    
    def __init__(self) -> None:
        self.state = self.read_config()

    def save_config(self):
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        with open(Path(CONFIG_DIR, "config.json"), "w") as outfile:
            outfile.write(json.dumps(self.state, indent=4))

    def read_config(self) -> dict:
        try:
            with open(Path(CONFIG_DIR, "config.json")) as f:
                result = json.load(f)
        except:
            result = DEFAULT_STATE

        return result
    
    