#!/usr/bin/python3
"""
A module that defines FileStorage class
"""
import json
from models.base_model import BaseModel
from models.user import User


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
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        obj_dict = {
                key: obj.to_dict() for key,
                obj in FileStorage.__objects.items()
                }
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing)
        If the file doesn’t exist, no exception should be raised
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    del value["__class__"]
                    obj_instance = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
