#!/usr/bin/python3
"""
Defines class Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"[Amenity] ({self.id}) {self.name}"

    def serialize(self):
        return {
            "name": self.name
        }

    @classmethod
    def deserialize(cls, data: dict):
        return cls(**data)
