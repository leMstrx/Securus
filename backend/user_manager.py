import json
from backend.encryption import decrypt_password, encrypt_password, generate_key

def create_user(username, password):
    key = generate_key()
    encrypted_password = encrypt_password(key, password)

    user_data = {
        "username": username, 
        "key": key.decode(),
        "password": encrypted_password.decode(),
    }

    #Read exisiting users
    users = get_users()

    #Append new user data to list
    users.append(user_data)

    with open("users.json", "w") as file: 
        json.dump(users, file, indent=2)

def get_users():
    try:
        with open("users.json", "r") as file:
            try:
                users = json.load(file)
            except json.JSONDecodeError:
                # Handle the case where the file is empty or not properly formatted
                users = []
    except FileNotFoundError:
        users = []

    return users

def find_user(username):
    users = get_users()
    for user in users:
        if user["username"] == username:
            return user
    return None