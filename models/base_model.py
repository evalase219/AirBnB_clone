#!/usr/bin/python3

"""
Here is where the base class of all the classes created in this
package is defined.

"""

import uuid
from datetime import datetime
from models.__init__ import storage


class BaseModel:
    """This model defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initializes all class instances

        Args:
            args (tuple): a tuple of argument names(currently not in use)
            kwargs (dict): key/value pairs representing attribute name : value
        """
        if kwargs:
            for key in kwargs:  # key=>attribute name, value=>attribute value
                if key != "__class__":  # all except for the `__class__` key

                    # convert these attributes from str back to datetime format
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.strptime(
                            kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())  # Create a unique id for each instance
            self.created_at = datetime.now()  # track created date & time
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return the class_name, id and dict of the created instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the `updated_at` attribute"""
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dict of attribute names of the instance"""
        self.__dict__['__class__'] = self.__class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()

        return self.__dict__
