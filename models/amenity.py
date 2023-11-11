#!/usr/bin/python3
"""Amenity class module"""
from model.base_model import BaseModel


class Amenity(BaseModel):
    """this class inherits from BaseModel"""
    name: str = ""
