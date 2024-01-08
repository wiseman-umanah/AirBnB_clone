#!/usr/bin/python3
import json


class FileStorage:
    __file_path = None
    __objects = {}

    def all(self):
        return self.__dict__(FileStorage.__objects)

    def save(self):
        with open(FileStorage.__file_path, "w") as fp:
            fp.write(json.dumps(self.all()))

    def reload(self):
        if FileStorage.__file_path is not None:
            with open(FileStorage.__file_path, "r") as fp:
                self.new(json.loads(fp.read()))

    def new(self, obj):
        key = f"{obj['__class__']}.{obj['id']}"
        FileStorage.__objects[key] = obj
