#!/usr/bin/python3
"""
    test_place module
"""
import unittest
from models.place import Place


class test_Place(unittest.TestCase):
    """ Tests for Place class """

    def test_created(self):
        """ check if an instance is correctly created """
        place1 = Place()
        self.assertIsInstance(place1, Place)

    def test_attributes(self):
        """ check if the instance has the proper attributes """
        place2 = Place()
        self.assertTrue(hasattr(place2, 'city_id'))
        self.assertTrue(hasattr(place2, 'user_id'))
        self.assertTrue(hasattr(place2, 'name'))
        self.assertTrue(hasattr(place2, 'description'))
        self.assertTrue(hasattr(place2, 'number_rooms'))
        self.assertTrue(hasattr(place2, 'number_bathrooms'))
        self.assertTrue(hasattr(place2, 'max_guest'))
        self.assertTrue(hasattr(place2, 'price_by_night'))
        self.assertTrue(hasattr(place2, 'latitude'))
        self.assertTrue(hasattr(place2, 'longitude'))
        self.assertTrue(hasattr(place2, 'amenity_ids'))

    def test_attr_type_and_value(self):
        """ check if the attributes have the correct type & default value """
        place3 = Place()
        self.assertEqual(type(place3.city_id), str)
        self.assertEqual(place3.city_id, "")

        self.assertEqual(type(place3.user_id), str)
        self.assertEqual(place3.user_id, "")

        self.assertEqual(type(place3.name), str)
        self.assertEqual(place3.name, "")

        self.assertEqual(type(place3.description), str)
        self.assertEqual(place3.description, "")

        self.assertEqual(type(place3.number_rooms), int)
        self.assertEqual(place3.number_rooms, 0)

        self.assertEqual(type(place3.number_bathrooms), int)
        self.assertEqual(place3.number_bathrooms, 0)

        self.assertEqual(type(place3.max_guest), int)
        self.assertEqual(place3.max_guest, 0)

        self.assertEqual(type(place3.price_by_night), int)
        self.assertEqual(place3.price_by_night, 0)

        self.assertEqual(type(place3.latitude), float)
        self.assertEqual(place3.latitude, 0.0)

        self.assertEqual(type(place3.longitude), float)
        self.assertEqual(place3.longitude, 0.0)

        self.assertEqual(type(place3.amenity_ids), list)
        self.assertEqual(place3.amenity_ids, [''])


if __name__ == '__main__':
    unittest.main()
