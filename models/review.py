#!/usr/bin/python3
"""Review class module"""
from model.base_model import BaseModel


class Review(BaseModel):
    """this class inherits from BaseModel"""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
