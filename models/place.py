#!/usr/bin/python3
from base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity

class Place(BaseModel):
    def __init__(self, city_id: str, user_id: str, name: str, description: str, number_rooms: int, number_bathrooms: int, max_guest: int, price_by_night: int, latitude: float, longitude: float, amenity_ids: List[str]):
        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids = amenity_ids

    def __str__(self):
        return f"[Place] ({self.id}) {self.name}"

    def serialize(self):
        return {
            "city_id": self.city_id,
            "user_id": self.user_id,
            "name": self.name,
            "description": self.description,
            "number_rooms": self.number_rooms,
            "number_bathrooms": self.number_bathrooms,
            "max_guest": self.max_guest,
            "price_by_night": self.price_by_night,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "amenity_ids": self.amenity_ids
        }

    @classmethod
    def deserialize(cls, data: dict):
        return cls(**data)
