#!/usr/bin/python3
"""
    file_storage module
"""

from os import path
import json
from models.base_model import BaseModel


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
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                print("read file")
                instances = json.load(file)
                print("instances: ")
                for k, v in instances.items():
                    self.__objects[k] = BaseModel(**v)
