#!/usr/bin/python3
"""FileStorage class module"""
import json
from json.decoder import JSONDecodeError
from models.base_model import BaseModel
from datetime import datetime


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

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        ser = {
                key: value.to_dict()
                for key, value in self.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(ser))

    def reload(self):
        """ deserializes the JSON file"""
        try:
            deser = {}
            with open(FileStorage.__file_path, "r") as f:
                deser = json.loads(f.read())
            FileStorage.__objects = {
                    key:
                        eval(obj["__class__"])(**obj)
                        for key, obj in deser.items()}
        except (FileNotFoundError, JSONDecodeError):
            pass
