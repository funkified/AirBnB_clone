#!/bin/usr/python3
"""
Module: review.py

Public attributes:
    - place_id
    - user_id
    - text
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    class Review inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
