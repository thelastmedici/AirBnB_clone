#!/usr/bin/python3
"""Amenity unittest"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import datetime
import time


class TestAmenity(unittest.TestCase):
    """amenity class TestCase"""

    def test_Amenity_class_membership_and_attributes(self):
        """Test Amenity class and if attributes are correct"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsNotNone(amenity.id)
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)
        self.assertIsNotNone(amenity.name)

    def test_Amenity_str(self):
        """Test Amenity str method"""
        amenity = Amenity()
        amenity_str = amenity.__str__
        self.assertIsInstance(amenity_str, str)
        self.assertDictEqual(eval(amenity_str), amenity.__dict__)

    def test_Amenity_save(self):
        """test Amenity save method"""
        amenity = Amenity()
        amenity.save()
        time.sleep(0.0001)
        self.assertNotEqual(amenity.updated_at, amenity.created_at)

    def test_Amenity_to_dict(self):
        """Test Amenity to_dict method if it creates accurate dictionary"""
        amenity = Amenity()
        amenity_dict = amenity.__dict__
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['id'], amenity.id)
        self.assertEqual(amenity_dict['__class__'], type(amenity).__name__)
        self.assertEqual(
            amenity_dict['created_at'], amenity.created_at.isoformat())
        self.assertEqual(
            amenity_dict['updated_at'], amenity.updated_at.isoformat())
        self.assertIsInstance(amenity.created_at, datetime.datetime)
        self.assertIsInstance(amenity.updated_at, datetime.datetime)

    def test_amenity_attr_type(self):
        """Amenity attributes are correct type"""
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)
        self.assertEqual(len(amenity.id), 36)
        self.assertIsInstance(amenity.created_at, datetime.datetime)
        self.assertIsInstance(amenity.updated_at, datetime.datetime)
        self.assertIsInstance(amenity.name, str)


if __name__ == '__main__':
    unittest.main()
