#!/usr/bin/python3
"""Defines a class for City"""
from models.base_model import BaseModel


class City(BaseModel):
    """This contains the details of City

    Attributes:
        state_id (str): empty for now
        name (str): empty for now"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
