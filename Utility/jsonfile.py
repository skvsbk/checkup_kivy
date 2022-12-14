import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR.joinpath("assets")


class JSONFile:
    def __init__(self, file_name):
        self._path_to_login_creds = DATA_DIR.joinpath(DATA_DIR, file_name)
        self.content = None

    def get_json(self):
        if self._path_to_login_creds.exists():
            try:
                with open(self._path_to_login_creds) as json_file:
                    self.content = json.loads(json_file.read())
            except:
                with open(self._path_to_login_creds, "w+") as json_file:
                    json_file.write("{}")
        return self.content

    def save_to_json(self, data):
        with open(self._path_to_login_creds, 'w') as json_file:
            json.dump(data, json_file)
