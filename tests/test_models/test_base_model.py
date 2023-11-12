#!/usr/bin/python3
"""unittest for BaseModel"""

"""unittest classes:
    TestBaseModel_inst
    TestBaseModel_save
    TestModel_to_dict
    """

import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
import os


class TestBaseModel_inst(unittest.TestCase):
    """unittesting for instantiation of BaseModel class"""

    def test_no_args_inst(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().value())
