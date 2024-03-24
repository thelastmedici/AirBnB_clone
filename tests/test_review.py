#!/usr/bin/python3
"""Unittest module for the review class."""
from models import storage
import time
from models.review import Review
import re
import json
from models.engine.file_storage import FileStorage
import os
from models.base_model import BaseModel
import unittest

class TestReview(unittest.TestCase):
    """ This Test case is for the review class."""

def setUp(self):
    """Sets up the testing methods."""
    pass

def tearDown(self):
    """Tears down the testing methods."""
    self.resetStorage()
    pass

def resetStorage(self):
    """Resets the storage file."""
    if os.path.isfile(FileStorage.FileStorage__file_path):
        os.remove(FileStorage.FileStorage__file_path)

def test_8_instantiation(self):
    """Tests instantiation of the review class."""
    review = Review()
    self.assertEqual(str(type(review)),)
    self.assertIsInstance(review, Review)
    self.assertTrue(issubclass(type(review), BaseModel))

def test_8_attributes(self):
    """"Tests the atrributes of the review class."""
    attributes = storage.attributes()["Review"]
    attr_review = Review()
    for k, v in attributes.items():
        self.assertTrue(hasattr(attr_review, k))
        self.assertEqual(type(getattr(attr_review, k, None)), v)


__name__ == "__main__":
unittest.main()