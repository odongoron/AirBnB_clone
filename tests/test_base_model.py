#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    
    def test_initialization(self):
        """ Test the initialization of the BaseModel instance """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))
    
    def test_to_dict(self):
        """ Test the to_dict method of BaseModel """
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 123
        model_dict = my_model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['name'], "Test Model")
        self.assertEqual(model_dict['my_number'], 123)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
    
    def test_save(self):
        """ Test the save method of BaseModel """
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)
    
    def test_str_method(self):
        """ Test the __str__ method of BaseModel """
        my_model = BaseModel()
        result = str(my_model)
        self.assertIn('[BaseModel]', result)
        self.assertIn(my_model.id, result)
    
    def test_create_from_dict(self):
        """ Test creating an instance from a dictionary """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        self.assertEqual(my_model.id, new_model.id)
        self.assertEqual(my_model.created_at, new_model.created_at)
        self.assertEqual(my_model.updated_at, new_model.updated_at)

if __name__ == "__main__":
    unittest.main()

