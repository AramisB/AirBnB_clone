#!/usr/bin/python3
"""
A module that defines FileStorage class
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    A class that serializes instances to a JSON file
    and deserializes JSON file to instances
    Attributes: __file_path(str)- path to the JSON file
    __objects(dict)- empty but will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return the dictionary __objects
        """
        return FileStorage.__objects
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        obj_name = obj.__class__.__name__
        FileStorage.__objects[f"{obj_name}.{obj.id}"] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        ob_dict = FileStorage.__objects
        obj_dict = {obj: ob_dict[obj].to_dict() for obj in ob_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)
    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
