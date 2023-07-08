#!/usr/bin/python3
"""
    test_review module
"""
import unittest
from models.review import Review


class test_Review(unittest.TestCase):
    """ Tests for Review class """
    def test_created(self):
        """ check if an instance is correctly created """
        rev1 = Review()
        self.assertIsInstance(rev1, Review)

    def test_attributes(self):
        """ check if the instance has the proper attributes """
        rev2 = Review()
        self.assertTrue(hasattr(rev2, 'place_id'))
        self.assertTrue(hasattr(rev2, 'user_id'))
        self.assertTrue(hasattr(rev2, 'text'))

    def test_attr_type_and_value(self):
        """ check if the attributes have the correct type & default value """
        rev3 = Review()
        self.assertEqual(type(rev3.place_id), str)
        self.assertEqual(rev3.place_id, "")

        self.assertEqual(type(rev3.user_id), str)
        self.assertEqual(rev3.user_id, "")

        self.assertEqual(type(rev3.text), str)
        self.assertEqual(rev3.text, "")


if __name__ == '__main__':
    unittest.main()
