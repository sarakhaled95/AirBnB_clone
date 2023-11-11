#!/usr/bin/python3
"""User class module"""
from models.base_model import BaseModel


class User(BaseModel):
    """this class inherits from BaseModel class"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
