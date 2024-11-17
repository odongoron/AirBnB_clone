#!/usr/bin/python3

# models/engine/file_storage.py
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    
    def all(self, cls=None):
        """Returns a dictionary of all objects, optionally filtered by class."""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects


    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                objects = json.load(f)
                classes = {
                    "BaseModel": BaseModel,
                    "User": User,
                    "State": State,
                    "City": City,
                    "Amenity": Amenity,
                    "Place": Place,
                    "Review": Review,
                }
                for obj_data in objects.values():
                    cls_name = obj_data["__class__"]
                    cls = classes.get(cls_name)
                    if cls:
                        self.__objects[f"{cls_name}.{obj_data['id']}"] = cls(**obj_data)
        except FileNotFoundError:
            pass

    def get(self, cls, obj_id):
        """
        Retrieves an object by class and ID.
        Returns the object if found, otherwise None.
        """
        key = f"{cls.__name__}.{obj_id}"
        return self.__objects.get(key, None)



    def count(self, cls):
        """Returns the number of instances of a class."""
        count = 0
        for key, obj in self.__objects.items():
            if isinstance(obj, cls):
                count += 1
        return count
