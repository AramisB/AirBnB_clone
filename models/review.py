
m base_model import BaseModel
from models.place import Place
from models.user import User

class Review(BaseModel):
    def __init__(self, place_id: str, user_id: str, text: str):
        self.place_id = place_id
        self.user_id = user_id
        self.text = text

    def __str__(self):
        return f"[Review] ({
