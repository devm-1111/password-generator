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

    try:
        with open(DATABASE_FILE, "r") as file:
            passwords = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        passwords = []

    passwords.append(password)

    with open(DATABASE_FILE, "w") as file:
        json.dump(passwords, file, indent=4)