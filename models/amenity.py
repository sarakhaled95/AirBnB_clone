#!/usr/bin/python3
"""Amenity class module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """this class inherits from BaseModel"""
    name: str = ""
