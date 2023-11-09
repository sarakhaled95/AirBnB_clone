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
    __objects = {}

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
        data = {}
        for key, value in self.__objects.items():
            class_name, obj_id = key.split('.')
            if class_name not in data:
                data[class_name] = {}
            data[class_name][obj_id] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(data, f)

    def reload(self):
        """ deserializes the JSON file"""
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
            for class_name, objects in data.items():
                for obj_id, obj_data in objects.items():
                    class_obj = globals()[class_name]
                    obj = class_obj(**obj_data)
                    self.__objects[f"{class_name}.{obj_id}"] = obj
        except (FileNotFoundError, JSONDecodeError):
            pass
