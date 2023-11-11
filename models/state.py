#!/usr/bin/python3
"""state class module"""
from models.base_model import BaseModel


class State(BaseModel):
    """this class inherits from BaseModel"""
    name: str = ""
