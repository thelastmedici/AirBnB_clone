#!/usr/bin/python3

"""review module"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Review class
    Attributes:
        place_id (str): palce id
        user_id (str): user id
        text (str): text
    """
    place_id = ""
    user_id = ""
    text = ""
