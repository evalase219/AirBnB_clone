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

            capture = {key_id: obj.to_dict() for key_id, obj in
                       FileStorage.__objects.items()}
            json.dump(capture, json_file)

    def reload(self):
        """Deserialize JSON file `__file_path` to __objects"""
        try:
            with open(f"{FileStorage.__file_path}", 'r') as json_file:
                holder = json.load(json_file)

                Base = None

                Base = importlib.import_module('models.base_model')

                FileStorage.__objects = {key_id: Base.BaseModel(obj)
                                         for key_id, obj in holder.items()}
        except FileNotFoundError:
            pass  # if the file does not exist don't do anything
