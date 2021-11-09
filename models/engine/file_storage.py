#!/usr/bin/python3
"""Private class attributes:
   - __file_path: string - path to the JSON file (ex: file.json)
   -__objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
Public instance methods:
   - all(self): returns the dictionary __objects
   - new(self, obj): sets in __objects the obj with key <obj class name>.id
   - save(self): serializes __objects to the JSON file (path: __file_path)
   - reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
"""

from models.base_model import BaseModel
import json

class FileStorage:
    """
    class that serializes instances to a
    JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        """
        """
        key = obj.__class__.name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """save to json """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as File:
            json.dump(__file_path, File)

    def reload(self):
        pass
