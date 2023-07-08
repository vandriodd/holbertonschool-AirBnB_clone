#!/usr/bin/python3
"""
    test_base_model module
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Tests for BaseModel class """
    def test_type_attributes(self):
        """ Check attribute types """
        base0 = BaseModel()
        self.assertEqual(type(base0.id), str)
        self.assertEqual(type(base0.created_at), datetime)
        self.assertEqual(type(base0.updated_at), datetime)

    def test_created(self):
        """ Check instances after update """
        base1 = BaseModel()
        base1.name = "Original name"
        self.assertEqual(base1.name, "Original name")
        base1.name = "New name"
        self.assertEqual(base1.name, "New name")
        base1.number = 10
        self.assertEqual(base1.number, 10)

    def test_instances(self):
        """ Check if object isInstance of BaseModel,
        and if its methods are of the correct type """
        base2 = BaseModel()
        self.assertTrue(isinstance(base2, BaseModel))
        self.assertTrue(isinstance(base2.id, str))
        self.assertTrue(isinstance(base2.created_at, datetime))
        self.assertTrue(isinstance(base2.updated_at, datetime))

    def test_save(self):
        """ Check save method """
        base3 = BaseModel()
        original_time = base3.updated_at
        base3.save()
        new_time = base3.updated_at
        self.assertNotEqual(original_time, new_time)

    def test_to_dict(self):
        """ Check to_dict method """
        base4 = BaseModel()
        base_dict = base4.to_dict()
        self.assertEqual(type(base_dict), dict)
        self.assertEqual(type(base_dict["created_at"]), str)
        self.assertEqual(type(base_dict["updated_at"]), str)

    def test_attributes_created(self):
        """ Check if attributes are properly setted """
        base5 = BaseModel()
        self.assertTrue(hasattr(base5, 'id'))
        self.assertTrue(hasattr(base5, 'created_at'))
        self.assertTrue(hasattr(base5, 'updated_at'))

    def test_str_(self):
        """ Check the overridden __str__ method """
        base6 = BaseModel()
        str_rep = f"[{base6.__class__.__name__}] ({base6.id}) {base6.__dict__}"
        self.assertEqual(str_rep, base6.__str__())


if __name__ == '__main__':
    unittest.main()
