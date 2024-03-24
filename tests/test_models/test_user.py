#!/usr/bin/python3
"""User unittest"""

import unittest
from models.user import User
from models.base_model import BaseModel
import datetime
import time


class TestUser(unittest.TestCase):
    """class TestCase"""

    def test_user_class_membership_and_attributes(self):
        """Test User class and if attributes are correct"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)
        self.assertIsNotNone(user.email)
        self.assertIsNotNone(user.password)
        self.assertIsNotNone(user.first_name)
        self.assertIsNotNone(user.last_name)

    def test_user_attribute_type(self):
        """Test user attribute type"""
        user = User()
        self.assertIsInstance(user.id, str)
        self.assertEqual(len(user.id, 36))
        self.assertIsInstance(user.created_at, datetime.datetime)
        self.assertIsInstance(user.updated_at, datetime.datetime)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_user_str(self):
        """Test user str method"""
        user = User()
        user_str = user.__str__
        self.assertIsInstance(user_str, str)
        self.assertDictEqual(eval(user_str), user.__dict__)

    def test_user_save(self):
        """test user save method"""
        user = User()
        user.save()
        time.sleep(0.0001)
        self.assertNotEqual(user.updated_at, user.created_at)

    def test_user_to_dict(self):
        """Test User to_dict method if it creates accurate dictionary"""
        user = User()
        user_dict = user.__dict__
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['id'], user.id)
        self.assertEqual(user_dict['__class__'], type(user).__name__)
        self.assertEqual(user_dict['created_at'], user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'], user.updated_at.isoformat())
        self.assertIsInstance(user.created_at, datetime.datetime)
        self.assertIsInstance(user.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
