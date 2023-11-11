#!/usr/bin/python3
"""FileStorage class module"""
import json
from json.decoder import JSONDecodeError
from models.base_model import BaseModel
from datetime import datetime
from models.engine.errors import *


class FileStorage:
    """class that serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path: str = "file.json"
    __objects = {}
    models = ("BaseModel")


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

    def find_by_id(self, model, obj_id):
        """finds and return model by its id"""
        M = FileStorage
        if model not in M.models:
            raise ModelNotFoundError(model)

        key = model + "." + obj_id
        if key not in M.__objects:
            raise InstanceNotFoundError(obj_id, model)

        return M.__objects[key]

    def del_by_id(self, model, obj_id):
        """finds and delets model by id"""
        M = FileStorage
        if model not in M.models:
            raise ModelNotFoundError(model)

        key = model + "." + obj_id
        if key not in M.__objects:
            raise InstanceNotFoundError(obj_id, model)

        del M.__objects[key]
        self.save()

    def find_all(self, model=""):
        """find all models"""
        if model and model not in FileStorage.models:
            raise ModelNotFoundError(model)
        result = []
        for key, value in FileStorage.__objects.items():
            if key.startswith(model):
                result.append(str(value))
        return result

    def update_1(self, model, xid, field, value):
        """updates an instance"""
        M = FileStorage
        if model not in M.models:
            raise ModelNotFoundError(model)

        key = model + "." + xid
        if key not in M.__objects:
            raise InstanceNotFoundError(xid, model)
        if field in ("id", "updated_at", "created_at"):
            return
        instance = M.__objects[key]
        try:
            value_type = type(instance.__dict__[field])
            instance.__dict__[field] = value_type(value)
        except KeyError:
            instance.__dict__[field] = value
        finally:
            instance.updated_at = datetime.now()
            self.save()
