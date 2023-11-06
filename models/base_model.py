#!/usr/bin/python3
"""BaseModel class module"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        """constructor method"""
        self.id = str(uuid.uuid4())
        self.create_at = datetime.now()
        self.update_at = self.create_at

    def update(self):
        """it will be updated every time you change your object"""
        self.update_at = datetime.now()
