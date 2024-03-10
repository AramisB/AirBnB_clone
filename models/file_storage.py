#!/usr/bin/python3
import json
from models.user import User

class FileStorage:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.users = self._load_users()

    def _load_users(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return [User.deserialize(user_data) for user_data in data]
        except FileNotFoundError:
            return []

    def _save_users(self):
        with open(self.file_path, "w") as file:
            json.dump([user.serialize() for user in self.users], file)

    def get_all(self):
        return self.users

    def get_by_id(self, user_id: int):
        return next((user for user in self.users if user.id == user_id), None)

    def create(self, user: User):
        self.users.append(user)
        self._save_users()

    def update(self, user_id: int, user: User):
        index = next((i for i, user in enumerate(self.users) if user.id == user_id), None)
        if index is not None:
            self.users[index] = user
            self._save_users()

    def delete(self, user_id: int):
        self.users = [user for user in self.users if user.id != user_id]
        self._save_users()
