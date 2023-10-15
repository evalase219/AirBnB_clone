#!/usr/bin/python3

"""
Here is where the base class of all the classes created in this
package is defined.

"""

import uuid
from datetime import datetime
import importlib


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
            storage = importlib.import_module("models.__init__").storage
            storage.new(self)

    def __str__(self):
        """Return the class_name, id and dict of the created instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the `updated_at` attribute"""
        self.updated_at = datetime.now()
        storage = importlib.import_module("models.__init__").storage
        storage.save()

    def to_dict(self):
        """Return a dict of attribute names of the instance"""

        clone = self.__dict__.copy()
        clone['__class__'] = self.__class__.__name__

        if isinstance(clone['created_at'], datetime) and isinstance(
                clone['updated_at'], datetime):
            clone['created_at'] = clone['created_at'].isoformat()
            clone['updated_at'] = clone['updated_at'].isoformat()

        return clone
