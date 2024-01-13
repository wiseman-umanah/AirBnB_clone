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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_room = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
