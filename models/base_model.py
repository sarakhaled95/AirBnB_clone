#!/usr/bin/python3
"""BaseModel class module"""
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """constructor method"""
        if kwargs == {}:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            return

        for key, value in kwargs.items():
            if key == '__class__':
                continue
            self.__dict__[key] = value
        if 'created_at' in kwargs:
            self.created_at = datetime.now()
        if 'updated_at' in kwargs:
            self.updated_at = datetime.now()

    def __str__(self):
        """string representation od class name and id"""
        return '[{}] ({}) {}'.\
               format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """it will be updated every time you change your object"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        my_dict = {**self.__dict__}
        my_dict['__class__'] = __class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        if isinstance(self.updated_at, str):
            my_dict['updated_at'] = datetime.fromisoformat(
                                    self.updated_at).isoformat()
        else:
            my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

    @classmethod
    def all(cls):
        """Retrive all current instance of class"""
        return models.storage.find_all(cls.__name__)

    @classmethod
    def show(cls, inst_id):
        """Retrive an istance"""
        return models.storage.find_by_id(cls.__name__, inst_id)

    @classmethod
    def create(cls, *args, **kwargs):
        """create instance"""
        new = cls(*args, **kwargs)
        return new.id

    @classmethod
    def destroy(cls, inst_id):
        """delete instance"""
        return models.storage.del_by_id(cls.__name__, inst_id)

    @classmethod
    def update(cls, inst_id, *args):
        """updates an instance"""
        if not len(args):
            print("** attribute name missing **")
            return
        if len(args) == 1 and isinstance(args[0], dict):
            args = args[0].items()
        else:
            args = [args[:2]]
        for arg in args:
            models.storage.update_1(cls.__name__, inst_id, *arg)

    @classmethod
    def count(cls, *args, **kwargs):
        """get the number of all current inst of classes"""
        return len(models.storage.find_all(cls.__name__))
