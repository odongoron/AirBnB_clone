#!/usr/bin/python3

from models import storage
from models.base_model import BaseModel

def test_save_reload():
    """ Test saving and reloading objects using FileStorage """
    # Create a new BaseModel instance
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()

    # Reload the stored objects
    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    # Check that the new object is in the storage
    self.assertTrue(f"BaseModel.{my_model.id}" in all_objs)

test_save_reload()

