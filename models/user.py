#!/usr/bin/python3
"""
Defines the User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a User

    Attributes:
    email(str) - empty
    password(str) - empty
    first_name(str) - empty
    last_name(str) - empty
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
