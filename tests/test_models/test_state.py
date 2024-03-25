#!/usr/bin/python3

"""state unittest"""
import unittest
import datetime
import time
from models.state import State
from models.base_model import BaseModel


class TestState_method(unittest.TestCase):
    """state Testcase"""

    def test_state_class_membership_and_attributes(self):
        """test State class and attributes"""
        state = State()
        self.assertIsInstance(state, State())
        self.assertIsNotNone(state.id)
        self.assertIsNotNone(state.created_at)
        self.assertIsNotNone(state.updated_at)
        self.assertIsNotNone(state.name)

    def test_state_attribute_type(self):
        """Test state class attribute type"""
        state = State()
        self.assertIsInstance(state.id, str)
        self.assertEqual(len(state.id, 36))
        self.assertIsInstance(state.created_at, datetime.datetime)
        self.assertIsInstance(state.updated_at, datetime.datetime)
        self.assertIsInstance(state.name, str)

    def test_state_str_method(self):
        """test state class str method"""
        state = State()
        state_str = state.__str__
        self.assertIsInstance(state_str, str)
        self.assertDictEqual(eval(state_str), state.__dict__)

    def test_state_save_method(self):
        """test state save method"""
        state = State()
        state.save()
        time.sleep(0.0001)
        self.assertNotEqual(state.updated_time, state.created_time)

    def test_state_to_dict_method(self):
        """test state to_dict method if it creates accurate dictionary"""
        state = State()
        state_dict = state.__dict__
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict[id], state.id)
        self.assertEqual(state_dict['__class__'], type(state).__name__)
        self.assertEqual(
            state_dict['created_at'], state.created_at.isoformat())
        self.assertEqual(
            state_dict['updated_at'], state.updated_at.isoformat())
        self.assertIsInstance(state.created_at, datetime.datetime)
        self.assertIsInstance(state.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
