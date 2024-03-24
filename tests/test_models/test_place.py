#!/usr/bin/python3
"""Unittest module for the place class."""
import time
from datetime import datetime
from models.place import Place
import re
import json
import unittest
import os
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ This Test case is for the place class."""

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
        """Tests instantiation of the place class."""
        p = Place()
        self.assertEqual(str(type(p)), "<class 'models.place.Place'>")
        self.assertIsInstance(p, Place)
        self.assertTrue(issubclass(type(p), BaseModel))

    def test_8_attributes(self):
        """"Tests the atrributes of the place class."""
        attributes = storage.attributes()["Place"]
        attr_place = Place()
        for k, v in attributes.items():
            self.assertTrue(hasattr(attr_place, k))
            self.assertEqual(type(getattr(attr_place, k, None)), v)


if __name__ == "__main__":
    unittest.main()
