#!/usr/bin/python3
"""Defines a class for Reviews"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This contains details of Reviews

    Attributes:
        place_id (str): empty for now
        user_id (str): empty for now
        text (str): empty for now"""
    place_id = ""
    user_id = ""
    text = ""
