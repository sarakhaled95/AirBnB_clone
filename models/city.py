#!/usr/bin/python3
"""city class module"""
from model.base_model import BaseModel


class city(BaseModel):
    """this class inhertits from BaseModel"""
    state_id: str = ""
    name: str = ""
