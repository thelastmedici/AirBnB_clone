#!/usr/bin/python3

"""city module"""

from models.base_model import BaseModel

class City(BaseModel):
    """city class
    Attributes:
        state_id (str): state id
        name (str): city name
    """

    state_id = ""
    name = ""
