#!/usr/bin/python3
"""
Module: city.py

Public attributes:
    - state_id
    - name
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Class City inherit from BaseModel
    """
    state_id = ""
    name = ""
