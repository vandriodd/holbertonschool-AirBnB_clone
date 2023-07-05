#!/usr/bin/python3
"""
    base_model module
"""

from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ BaseModel class """

    def __init__(self):
        """ Initializes an instance of BaseModel class """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Override the __str__ method so the print() function
        returns a specific string
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates attribute updated_at with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns an instance in dict format """
        my_dict = self.__dict__
        my_dict.update({'__class__': self.__class__.__name__})
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict
