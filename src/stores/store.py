import json
from os import path


class Store():
    def __init__(self, path_to_file) -> None:
        self.path_to_file = path_to_file

    def _change_path_to_file(self, new_path_to_file):
        self.path_to_file = new_path_to_file;

    def _read_or_create(self, fn_init):
        if path.isfile(self.path_to_file):
            with open(self.path_to_file, 'r') as file:
                return json.load(file)

        with open(self.path_to_file, 'w+') as file:
            content = fn_init()
            json.dump(content, file)
            return content

    def _save(self, data):
        with open(self.path_to_file, 'w+') as file:
            json.dump(data, file)
