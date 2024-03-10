#!/usr/bin/python3
m models.user import User
from storage.file_storage import FileStorage

def show_users():
    storage = FileStorage("users.json")
    users = storage.get_all()
    for user in users:
        print(user)

def create_user():
    email = input("Email: ")
    password = input("Password: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    user = User(email, password, first_name, last_name)
    storage = FileStorage("users.json")
    storage.create(user)
    print("User created successfully.")

def update_user():
    user_id = int(input("User ID: "))
    storage = FileStorage("users.json")
    user = storage.get_by_id(user_id)
    if user is not None:
        email = input("Email: ")
        password = input("Password: ")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        updated_user = User(email, password, first_name, last_name)
        storage.update(user_id, updated_user)
        print("User updated successfully.")
    else:
        print("User not found.")

def delete_user():
    user_id = int(input("User ID: "))
    storage = FileStorage("users.json")
    user = storage.get_by_
