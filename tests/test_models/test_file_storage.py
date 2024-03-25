#!/usr/bin/python3
"""Unittest module for the FileStorage class"""
import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import re
import json
import os

class TestFileStorage(unittest.TestCase):
    """Test Cases for the FileStorage class."""

    def setUp(self):
        """ test methods set up"""
        pass

    def resetStorage(self):
        """Resets FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """method that Tears down test methods."""
        self.resetStorage()
        pass

    def test_5_instantiation(self):
        """Tests instantiation of storage class."""
        self.assertEqual(type(storage).__name__, "FileStorage" )

    def test_3_init_no_args(self):
        """Tests initialization method with no arguments"""
        self.resetStorage()
        with self.assertRaises(TypeError) as err:
            FileStorage.__init__()
        message = "'initialization of object' object needs an argument"
        self.assertEqual(str(err.exception), message)


    def init_with_many_args(self):
        """Test Initialization with many arguments"""
        self.resetStorage()
        with self.assertRaises(TypeError) as err:
            b = FileStorage(0,1,2,3,4,5,6,7,8,9)
        message = "object method takes no parameters"
        self.assertEqual(str(err.exception), message)

    def test_5_attributes(self):
        """Test class attributes."""
        self.resetStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"),{})

    def help_test_all(self, classname):
        """Helper tests all method for classname."""
        self.resetStorage()
        self.assertEqual(storage.all(),{})
        new_obj= storage.classes()[classname]()
        storage.new(new_obj)
        key = f"{type(new_obj).__name__}, {new_obj.id}"
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], new_obj)


    def all_base_model(self):
        """TEST all method of the BaseModel class"""
        self.help_test_all("BaseModel")


    def all_user(self):
        """this method test the all method for user"""
        self.help_test_all("User")

    def all_state(self):
        """test the all method for state"""
        self.help_test_all("State")

    def all_city(self):
        """test the all method for city"""
        self.help_test_all("City")

    def all_amenity(self):
        """test the alll method for amenities"""
        self.help_test_all("Amenity")

    def all_place(self):
        """test the all method for place"""
        self.help_test_all("Place")

    def all_review(self):
        """test the all method for Review"""

    