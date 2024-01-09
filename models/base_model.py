#!/usr/bin/python3
import datetime
import uuid
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        if args:
            models.storage.new()
        elif kwargs:
            self.id = kwargs["id"]
            self.created_at = datetime.datetime.fromisoformat(
                kwargs["created_at"])
            self.updated_at = datetime.datetime.fromisoformat(
                kwargs["updated_at"])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        if isinstance(self.updated_at, datetime.datetime):
            self.updated_at = datetime.datetime.isoformat(self.updated_at)
        if isinstance(self.created_at, datetime.datetime):
            self.created_at = datetime.datetime.isoformat(self.created_at)
        result = self.__dict__.copy()
        result["__class__"] = __class__.__name__

        return result
