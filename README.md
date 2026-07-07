# Password Generator

A Python tool that generates secure random passwords with customizable character sets and stores them in a JSON file.

## Features

* Generate secure random passwords
* Choose the password length
* Include or exclude:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Symbols
* Store generated passwords in a JSON file
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
 Password Generator v1.1
==============================

Password length: 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): n

Generated password:

Pq4LmX9AbT2c

Password saved to passwords.json
```

## Output

Generated passwords are stored in `passwords.json`.

Example:

```json
[
    "Pq4LmX9AbT2c"
]
```

## Technologies

* Python
* secrets
* string
* JSON
