#!/usr/bin/python3
"""
    test_base_model module
"""

import unittest
from models.base_model import BaseModel

class test_base_model(unittest.TestCase):
    """ Tests BaseModel class """
    base_model = BaseModel()

if __name__ == "__main__":
    unittest.main()
