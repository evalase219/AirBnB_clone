#!/usr/bin/python3

"""
Here is where the base class of all the classes created in this
package is defined.

"""

import uuid
from datetime import datetime


class BaseModel:
    """This model defines all common attributes/methods for other classes"""
    def __init__(self):
        """Initializes all class instances"""
        self.id = str(uuid.uuid4())  # Create a unique id for each instance
        self.created_at = datetime.now()  # Keep track of created date and time
        self.updated_at = datetime.now()

    def __str__(self):
        """Return the class_name, id and dict of the created instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the `updated_at` attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dict of attribute names of the instance"""
        self.__dict__['__class__'] = self.__class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()

        return self.__dict__
