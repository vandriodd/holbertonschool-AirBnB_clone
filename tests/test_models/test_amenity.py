#!/usr/bin/python3
"""
    test_amenity module
"""
import unittest
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    """ Tests for Amenity class """

    def test_created(self):
        """ check if an instance is correctly created """
        amenity1 = Amenity()
        self.assertIsInstance(amenity1, Amenity)

    def test_attribute(self):
        """ check if the instance has the proper attribute """
        amenity2 = Amenity()
        self.assertTrue(hasattr(amenity2, 'name'))

    def test_attr_type_and_value(self):
        """ check if the attribute has the correct type & default value """
        amenity3 = Amenity()
        self.assertEqual(type(amenity3.name), str)
        self.assertEqual(amenity3.name, "")


if __name__ == '__main__':
    unittest.main()
