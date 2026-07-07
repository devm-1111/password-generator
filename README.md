# Password Generator

A Python tool that generates secure random passwords with customizable character sets, stores them in a JSON file, and allows you to manage saved passwords through an interactive menu.

## Features

* Generate secure random passwords
* Choose the password length
* Include or exclude:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Symbols
* Save generated passwords to a JSON file
* View saved passwords
* Clear password history
* Interactive menu
* Uses Python's `secrets` module for secure password generation
* No external dependencies required

## Requirements

* Python 3.x

## Installation

```bash
git clone https://github.com/devm-1111/password-generator.git
cd password-generator
```

## Usage

```bash
python main.py
```

Example:

```text
==============================
 Password Generator v1.2
==============================

1. Generate password
2. View saved passwords
3. Clear password history
4. Exit

Select an option:
```

## Output

Generated passwords are stored in `passwords.json`.

Example:

```json
[
    "A7#mQ!2xLp@9",
    "Pq4LmX9AbT2c",
    "80E&,6GA"
]
```

## Technologies

* Python
* secrets
* string
* JSON
