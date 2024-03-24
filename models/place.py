#!/usr/bin/python3

"""place module"""

from models.base_model import BaseModel


class Place(BaseModel):
    """place class
    Attributes:
        city_id (str): city id
        user_id (str): user id
        name (str): name
        description (str): description
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_quest (int): maximum number of quest
        price_by_night (int): price for a night
        latitude (float): latitude
        longitude (float): longitude
        amenity_ids (str): list of amenity ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
