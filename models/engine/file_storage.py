#!/usr/bin/python3
"""FileStorage class module"""
import json


class FileStorage:
    """class that serializes instances to a JSON file and 
    deserializes JSON file to instances"""
    __file_path: str = "file.json"
    __objects: dict = {}

    def __init__(self):
        """constructor"""
        pass

    def all(self):
        """returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj


