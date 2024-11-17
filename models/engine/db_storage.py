#!/usr/bin/python3

# models/engine/db_storage.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://user:password@localhost/db_name', pool_pre_ping=True)

    def all(self, cls=None):
        results = {}
        if cls:
            for obj in self.__session.query(cls).all():
                results[f"{cls.__name__}.{obj.id}"] = obj
        else:
            for cls in [User, State, City, Amenity, Place, Review]:
                for obj in self.__session.query(cls).all():
                    results[f"{obj.__class__.__name__}.{obj.id}"] = obj
        return results

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()


    def get(self, cls, id):
        """Retrieve one object based on the class and ID."""
        return self.__session.query(cls).get(id)

    def count(self, cls=None):
        """Count the number of instances in storage."""
        if cls:
            return self.__session.query(cls).count()
        else:
            total = 0
            for cls in [User, State, City, Amenity, Place, Review]:
                total += self.__session.query(cls).count()
            return total

