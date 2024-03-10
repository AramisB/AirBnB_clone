#!/usr/bin/python3
"""
Defines the Review class
"""


class Review(BaseModel):
    """
    Represents a review

    Attributes:
    place_id(str): The place id
    user_id(str): the user id
    text(str): the text of the review
    """

    place_id = ""
    user_id = ""
    text = ""
