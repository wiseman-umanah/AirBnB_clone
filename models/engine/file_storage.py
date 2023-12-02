#!/usr/bin/python3
import json


class FileStorage:
    def __init__(self, file_path=None, objects=None):
        self.__file_path = file_path
        self.__objects = objects

    @property    
    def all(self):
        return self.__objects
    
    @all.setter
    def  new(self, obj):
        key = f"{obj.__class__.__name__ } + {self.id}"
        self.__objects["key"] = key
    
    def save(self):
        with open(self.__file_path, "w") as fp:
            fp.write(json.dumps(self.all()))
    
    def reload(self):
        if self.__file_path != None:
            with open(self.__file_path, "r") as fp:
                 self.new(json.loads(fp.read()))
