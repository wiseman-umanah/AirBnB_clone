#!/usr/bin/python3
"""Defines the User class for user's details"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class saves the details of the User

    Attributes:
        email (str): empty email; updated later
        password (str): empty for now
        first_name (str): empty for now
        last_name (str): empty for now"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.lastname = ""
