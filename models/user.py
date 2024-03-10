#!/usr/bin/python3
m base_model import BaseModel
from typing import List

class User(BaseModel):
    def __init__(self, email: str, password: str, first_name: str, last_name: str):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"

    def serialize(self):
        return {
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name
        }

    @classmethod
    def deserialize(cls, data: dict):
        return cls(**data)
