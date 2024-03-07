#!/usr/bin/python3
"""
A module that defines the BaseModel class
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    Represents the model of HBNB project
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel instance
        """
	time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
	for len(kwargs)!= 0:
		for key, value in kwargs.items():
			if key == "created_at" or key == "updated_at":
				self.__dict__[key] = datetime.strptime(value, time_format)
	else:
		self. __dict__[key] = value
    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.today()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Returns the dtring representation of the BaseModel instance
        """
        cls_name = self.__class__.__name__
        return f"[{cls_name}] ({self.id}) {self.__dict__}"
