#!/usr/bin/python3

# models/review.py
from models.base_model import BaseModel

class Review(BaseModel):
    place_id = ""    # Place.id
    user_id = ""     # User.id
    text = ""