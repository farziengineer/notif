from io_.read_write import Reader

import json


class JsonReader(Reader):
    def __init__(self):
        self._inp = None

    def read(self, path):
        with open(path) as f:
            self._inp = json.loads(f.read())
        return self._inp