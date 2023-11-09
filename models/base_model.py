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
            my_dict['updated_at'] = datetime.fromisoformat\
                    (self.updated_at).isoformat()
        else:
            my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
