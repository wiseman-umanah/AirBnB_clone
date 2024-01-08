#!/usr/bin/python3
import datetime
import uuid


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.update_at = datetime.datetime.now()

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.update_at = datetime.datetime.now()

    def to_dict(self):
        self.update_at = datetime.datetime.isoformat(self.update_at)
        self.created_at = datetime.datetime.isoformat(self.created_at)
        self.__dict__["__class__"] = __class__.__name__
        return (self.__dict__)
