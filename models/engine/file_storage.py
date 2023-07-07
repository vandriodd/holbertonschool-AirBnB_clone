#!/usr/bin/python3
"""
    file_storage module
"""

from os import path
import json


class FileStorage:
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ placeholder """
        return self.__objects

    def new(self, obj):
        """ placeholder """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Serializes """
        my_dict = {}
        for k, v in self.__objects.items():
            my_dict[k] = v.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(my_dict, file)

    def reload(self):
        """ placeholder """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity,
                   "Place": Place, "Review": Review}
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                instances = json.load(file)
            for k, v in instances.items():
                class_name = k.split('.')[0]
                self.__objects[k] = classes[class_name](**v)
