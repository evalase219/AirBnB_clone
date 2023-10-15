#!/usr/bin/python3

"""

City module inherited from the basemodel.

"""

from models.base_model import BaseModel

class City(BaseModel):
    """The user's city

    Attributes:
        state_id (str): The user's state identification
        name (str): The name of the user's city
    """

    state_id = ""
    name = ""
