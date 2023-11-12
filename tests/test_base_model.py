#!/usr/bin/python3
"""unittest for BaseModel"""
import unittest
import models
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_inst(unittest.TestCase):
    """unittesting for intantatiation of the basemodel class"""

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_values_stored_in_objects(self):
        self.assertIn(BaseModel, models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
