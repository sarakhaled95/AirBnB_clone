#!/usr/bin/python3
"""unittest for BaseModel
unittest classes:
    TestBaseModel_inst
    TestBaseModel_save
    TestModel_to_dict
    """
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
import os
from time import sleep


class TestBaseModel_inst(unittest.TestCase):
    """unittesting for instantiation of BaseModel class"""

    def test_no_args_inst(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_publicStr(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unique_ids(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_diff_created_at(self):
        m1 = BaseModel()
        sleep(0.05)
        m2 = BaseModel()
        self.assertLess(m1.created_at, m2.created_at)

    def test_diff_updated_at(self):
        m1 = BaseModel()
        sleep(0.05)
        m2 = BaseModel()
        self.assertLess(m1.updated_at, m2.updated_at)

    def test_str_representation(self):
        dt = datetime.now()
        dt_repr = repr(dt)
        m = BaseModel()
        m.id = "98765"
        m.created_at = m.updated_at = dt
        m_str = m.__str__()
        self.assertIn("[BaseModel] (98765)", m_str)
        self.assertIn("'id': '98765'", m_str)
        self.assertIn("'created_at': " + dt_repr, m_str)
        self.assertIn("'updated_at': " + dt_repr, m_str)

    def test_with_args_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        m = BaseModel("30", id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(m.id, "123")
        self.assertEqual(m.created_at, dt)
        self.assertEqual(m.updated_at, dt)


if __name__ == "__main__":
    unittest.main()
