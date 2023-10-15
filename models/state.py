#!/usr/bin/python3

"""
State module inherited from the base class.
"""

from models.base_model import BaseModel

class State(BaseModel):
    """The state of the user.

    Attribute:
        name (str): The name of user's state.
    """

    name = ""
