#!/usr/bin/python3

"""

Review module inherited from the basemodel.

"""
from models.base_model import BaseModel

class Review(BaseModel):
    """Represent a review  of the place

    Attributes:
        place_id (str): The plac identification
        user_id (str): The user identification
        text (str): The text of the review
    """
    place_id = ""
    user_id = ""
    text = ""
