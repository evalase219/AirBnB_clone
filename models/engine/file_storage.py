#!/usr/bin/python3

"""
File_storage for now is the primary means of storing
and persisting all created class instances of the application

"""

import json


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
            FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        """Serialize `__objects` to JSON file `__file_path`"""
        with open(f"{FileStorage.__file_path}", 'w') as json_file:
            print("Loading into file.......")
            json.dump(FileStorage.__objects, json_file)

    def reload(self):
        """Deserialize JSON file `__file_path` to __objects"""
        try:
            with open(f"{FileStorage.__file_path}", 'r') as json_file:
                print("Reloading file.......")
                FileStorage.__objects = json.load(json_file)
        except FileNotFoundError:
            pass  # if the file does not exist don't do anything
