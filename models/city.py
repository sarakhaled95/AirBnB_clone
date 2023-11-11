#!/usr/bin/python3
"""city class module"""
from models.base_model import BaseModel


class City(BaseModel):
    """this class inhertits from BaseModel"""
    state_id: str = ""
    name: str = ""
