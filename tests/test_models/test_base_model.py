#!/usr/bin/python3

"""base_model unittest"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import datetime
import time


class TestBaseModel(unittest.TestCase):
    """BaseModel TestCase"""
    def test_BaseModel_class_membership_and_attributes(self):
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIsNotNone(base.id)
        self.assertIsNotNone(base.created_at)
        self.assertIsNotNone(base.updated_at)

    def test_BaseModel_attribute_type(self):
        """Test BaseModel attribute type"""
        base = BaseModel()
        self.assertIsInstance(base.id, str)
        self.assertEqual(len(base.id, 36))
        self.assertIsInstance(base.created_at, datetime.datetime)
        self.assertIsInstance(base.updated_at, datetime.datetime)

    def test_BaseModel_str(self):
        """Test BaseModel str method"""
        base = BaseModel()
        base_str = base.__str__
        self.assertIsInstance(base_str, str)
        self.assertDictEqual(eval(base_str), base.__dict__)

    def test_BaseModel_save(self):
        """test BaseModel save method"""
        base = BaseModel()
        base.save()
        time.sleep(0.0001)
        self.assertNotEqual(base.updated_at, base.created_at)

    def test_BaseModel_to_dict(self):
        """Test BaseModel to_dict method if it creates accurate dictionary"""
        base = BaseModel()
        base_dict = base.__dict__
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict['id'], base.id)
        self.assertEqual(base_dict['__class__'], type(base).__name__)
        self.assertEqual(base_dict['created_at'], base.created_at.isoformat())
        self.assertEqual(base_dict['updated_at'], base.updated_at.isoformat())
        self.assertIsInstance(base.created_at, datetime.datetime)
        self.assertIsInstance(base.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
