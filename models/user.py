#!/usr/bin/python3

"""
User class used to manage user instances are defined in this module

"""

from models.base_model import BaseModel


class User(BaseModel):
    """Manages user instances"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
