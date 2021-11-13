#!/usr/bin/python3
"""
Module: state.py

Public instances attributes:
    - name
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Class User inherited from BaseModel
    Will create State for User
    """
    name = ""
