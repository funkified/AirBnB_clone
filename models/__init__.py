#!/usr/bin/python3
"""
Constructor: __init__.py

A package or directory:
   - Let the interpreter know that a directory contains code for Python Module
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
