#!/usr/bin/python3

"""

Amenity module inherited from the basemodel.

"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Represent the user's amenity.

    Attribute:
        name (str): The name of the amenity.
    """

    name = ""
