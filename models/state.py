#!/usr/bin/python3
"""Defines the State class for User"""
from models.base_model import BaseModel


class State(BaseModel):
    """This class saves the name of the State

    Attributes:
        name (str): empty string; updated later"""
    name = ""
