#!/usr/bin/python3
"""Defines a class for Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """This contains details of user's region

    Attributes:
        city_id (str): empty for now
        user_id (str): empty for now
        name (str): empty for now
        description (str): empty for now
        number_room (int): initialized to 0
        number_bathrooms (int): initialized to 0
        max_guest (int): initialized to 0
        price_by_night (int): initialized to 0
        latitude (float): initialized to 0.0
        longitude (float): initialized to 0.0
        amenity_ids (list): empty list for now"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_room = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
