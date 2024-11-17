#!/usr/bin/python3

# models/place.py
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Place(BaseModel, Base):
    __tablename__ = 'places'
    
    name = Column(String(128), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    city = relationship("City", back_populates="places")       
    user_id = ""        
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []    

