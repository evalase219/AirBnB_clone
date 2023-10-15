#!/usr/bin/python3

"""

Place module that is inherited from basemodel

"""

from models.base_model import BaseModel

class Place(BaseModel):
    """Represent the user's place

    Attributes:
        city_id (str): The city identification of the user.
        user_id (str): The user identification
        name (str): The name of the place
        description (str): The description of the place.
        number_rooms (int): The number of the rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guest it can accomodate.
        price_by_night (int): The price per night.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): The list of the amenity identification.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
