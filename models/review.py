#!/usr/bin/python3
"""Defines a class for Reviews"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This contains details of Reviews

    Attributes:
        place_id (str): empty for now
        user_id (str): empty for now
        text (str): empty for now"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
