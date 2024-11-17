#!/usr/bin/python3

# models/state.py
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class State(BaseModel, Base):
    """Represents a state for a MySQL database."""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state") 
