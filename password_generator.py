import json
import secrets
import string

DATABASE_FILE = "passwords.json"


def generate_password(length):

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password


def save_password(password):

    try:
        with open(DATABASE_FILE, "r") as file:
            passwords = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        passwords = []

    passwords.append(password)

    with open(DATABASE_FILE, "w") as file:
        json.dump(passwords, file, indent=4)