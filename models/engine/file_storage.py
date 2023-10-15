#!/usr/bin/python3

"""
File_storage for now is the primary means of storing
and persisting all created class instances of the application

"""

import json
import importlib


class FileStorage:
    """
    Responsible for serialization and deserialization of
    of class instances
    """
    __file_path = "file.json"
    __objects = {}

    @staticmethod
    def cls_selector(**obj):
        """
        Select the appropriate class to handle deserialization

        Args:
            obj (dict): dictionary of the given instance

        Return:
            the correct class to be used
        """
        Base = None

        if obj['__class__'] == "BaseModel":
            Base = importlib.import_module('models.base_model')
            return Base.BaseModel(**obj)
        elif obj['__class__'] == "User":
            Base = importlib.import_module('models.user')
            return Base.User(**obj)
        elif obj['__class__'] == "State":
            Base = importlib.import_module('models.state')
            return Base.State(**obj)
        elif obj['__class__'] == "City":
            Base = importlib.import_module('models.city')
            return Base.City(**obj)
        elif obj['__class__'] == "Amenity":
            Base = importlib.import_module('models.amenity')
            return Base.Amenity(**obj)
        elif obj['__class__'] == "Place":
            Base = importlib.import_module('models.place')
            return Base.Place(**obj)
        elif obj['__class__'] == "Review":
            Base = importlib.import_module('models.review')
            return Base.Review(**obj)
        else:
            return Base

    def all(self):
        """Returns the dictionary: (__objects) """
        return FileStorage.__objects

    def new(self, obj):
        """
        Set obj argument by the key [<class name>.id] and add
        to the `__objects` dictionary

        Args:
            obj (object): object to process
        """
        if obj:
            FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serialize `__objects` to JSON file `__file_path`"""
        with open(f"{FileStorage.__file_path}", 'w') as json_file:

            self.capture = {key_id: obj.to_dict() for key_id, obj in
                            FileStorage.__objects.items()}
            json.dump(self.capture, json_file)

    def reload(self):
        """Deserialize JSON file `__file_path` to __objects"""
        try:
            with open(f"{FileStorage.__file_path}", 'r') as json_file:
                self.hold = json.load(json_file)

                class_selector = FileStorage.cls_selector
                FileStorage.__objects = {key_id: class_selector(**obj)
                                         for key_id, obj in self.hold.items()}
        except FileNotFoundError:
            pass  # if the file does not exist don't do anythinga
