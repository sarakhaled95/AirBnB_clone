#!/usr/bin/python3
"""Initializes Module Global Variables"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
