#!/usr/bin/python3
from model import Base
class State(BaseModel):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"[State] ({self.id}) {self.name}"

    def serialize(self):
        return {
            "name": self.name
        }

    @classmethod
    def deserialize(cls, data: dict):
        return cls(**data)
