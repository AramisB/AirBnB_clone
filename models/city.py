#!/usr/bin/python3
from base_model import BaseModel
from models.state import State

class City(BaseModel):
    def __init__(self, state_id: str, name: str):
        self.state_id = state_id
        self.name = name

    def __str__(self):
        return f"[City] ({self.id}) {self.name} in {State.get_by_id(self.state_id).name}"

    def serialize(self):
        return {
            "state_id": self.state_id,
            "name": self.name
        }

    @classmethod
    def deserialize(cls, data: dict):
        return cls(**data)
