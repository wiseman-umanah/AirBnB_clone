#!/usr/bin/python3
"""Defines the class for Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This contains details for Amenity

    Attributes:
        name (str): empty for now"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
