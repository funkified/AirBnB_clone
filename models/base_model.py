#!/usr/bin/python3

"""
Module: base_model.py

Methods:
   - __init__
   - __str__
   - save(self)
   - to_dict(self)

Public instances attrs:
   - id
   - created_at
   - updated_at

ImportModules:
   - uuid -> stand for Universally Unique Identifiers
   - datetime
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    The base class for all the subclasses
    """

    def __init__(self, *args, **kwargs):
        """
        Intialize attrs when an instance is created
        """
        if kwargs:
            for key, value in kwargs.items():
                if hasattr(self, "created_at"):
                    # if key == "created_at":
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                if hasattr(self, "updated_at"):
                    # if key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                        setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of the class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Will update the updated_at with current time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of __dict__ instances
        """
        dic = {}
        dic["__class__"] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dic[key] = value.isoformat()
            else:
                dic[key] = value
        return dic
