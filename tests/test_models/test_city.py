#!/usr/bin/python3
"""Unittest module for the city class."""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel

class TestCity (unittest.TestCase):
    """This Test case is for the city class."""

    def setUp(self):
        """Sets up the testing methods."""
        pass

    def tearDown(self):
        """Tears down the testing methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of the city class."""
        city = City()
        self.assertEqual(str(type(city)), "<class 'models.city.City'>")
        self.assertIsInstance(city, City)
        self.assertTrue(issubclass(type(city), BaseModel))

    def test_8_attributes(self):
        """"Tests the atrributes of the city class."""
        attr = storage.attributes()["City"]
        attr_city = City()
        for k, v in attr.items():
            self.assertTrue(hasattr(attr_city, k))
            self.assertEqual(type(getattr(attr_city, k, None)), v)

if __name__ == "__main__":
    unittest.main()
