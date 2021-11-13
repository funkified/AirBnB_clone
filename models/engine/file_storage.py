#!/usr/bin/python3
"""
Module: file_storage.py

Private class attributes:
   - __file_path
     - a string path to the JSON file (In this case "file.json")
   -__objects
     - An empty dictionary that will store all objects. For ClassName will be
       saved like: Base.id -> format -> "{}.{}".format(self.className, self.id)

Public instance methods:
   - all(self)
   - new(self, obj)
   - save(self)
   - reload(self)
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
        """
        Return all objects of the dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        Creating a new key for the base.id format
        and adding to the dictionary
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Serializing to a json string
        We iterate through the dictionary items, give them to key,value
        Calling "to_dict" method to create a dictionary with our format
        then we give all the objects key/val to our new dict so we can save it
        in as Json File
        """
        new_dict = {}

        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as File:
            json.dump(new_dict, File)

    def reload(self):
        """
        Deserialize from a json File
        Using try/except to handle exception if need it,
        We are going to try if the file exist to read it
        Then convert everything as a dictionary object like before
        if doesn't exist then pass since no exception need it right now
        """
        try:
            with open(self.__file_path, "r") as File:

                newDic = json.load(File)

                for key, value in newDic.items():

                    classes = key.split(".")

                    self.__objects[key] = eval(classes[0])(**value)

        except FileNotFoundError:
            pass
