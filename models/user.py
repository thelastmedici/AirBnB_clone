#!/usr/bin/python3

"""user module"""
from models.base_model import BaseModel

class User(BaseModel):

    """ Represents class User,
    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): user's first name
        last_name (str): user's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
