#!/usr/bin/python3
"""
Module: user.py

Public instances attributes:
    - email
    - password
    - first_name
    - last_name
"""

from models.base_model import BaseModel

class User(BaseModel):
    """class for User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
