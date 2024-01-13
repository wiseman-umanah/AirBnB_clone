#!/usr/bin/python3
"""
This is the Base Model

The backbone of the overall program

This is where other classes inherit from
"""
import datetime
import uuid
import models


class BaseModel:
    """This class contains functionality for building,
    constructing and creating a new instance of any class

    Methods:
        save: updates time and saves new instance to file
        dict: converts the instance to a dictionary
    """
    def __init__(self, *args, **kwargs):
        """Initializes a new instance from arguments

        Args:
            args: list of instance data
            kwargs: dictionary representation of instance
        """    
        if len(kwargs) != 0:
            self.id = kwargs["id"]
            self.created_at = datetime.datetime.fromisoformat(
                kwargs["created_at"])
            self.updated_at = datetime.datetime.fromisoformat(
                kwargs["updated_at"])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Function to return the string representation of instance

        Return:
            [<class.name>] (<classId>) <classAttributes>)
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Function updates time and saves new instance to file"""
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Function converts the instance to a dictionary

        Return:
            The new dictionary that contains all the class attributes
        """
        if isinstance(self.updated_at, datetime.datetime):
            self.updated_at = datetime.datetime.isoformat(self.updated_at)
        if isinstance(self.created_at, datetime.datetime):
            self.created_at = datetime.datetime.isoformat(self.created_at)
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__

        return result
