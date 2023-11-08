#!/usr/bin/python3
"""BaseModel class module"""
import json
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        """constructor method"""
        self.id = str(uuid.uuid4())
        self.create_at = datetime.now().isoformat()
        self.update_at = self.create_at

    def __str__(self):
        """string representation od class name and id"""
        return '[{}] ({}) {}'.\
                format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """it will be updated every time you change your object"""
        self.update_at = datetime.now().isoformat()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        my_dict = self.__dict__
        my_dict['__class__'] = __class__.__name__
        return my_dict
