#!/usr/bin/python3

# models/city.py
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship  # Import relationship
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """Represents a city for a MySQL database."""
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")