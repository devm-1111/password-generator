import json
import secrets
import string

DATABASE_FILE = "passwords.json"


def generate_password(length, uppercase, lowercase, numbers, symbols):

    characters = ""

    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if numbers:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password


def save_password(password):

    passwords = load_passwords()

    passwords.append(password)

    with open(DATABASE_FILE, "w") as file:
        json.dump(passwords, file, indent=4)


def load_passwords():

    try:
        with open(DATABASE_FILE, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def clear_passwords():

    with open(DATABASE_FILE, "w") as file:
        json.dump([], file, indent=4)