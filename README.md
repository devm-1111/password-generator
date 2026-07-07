# Password Generator

A simple Python tool that generates secure random passwords and stores them in a JSON file.

## Features

* Generate secure random passwords
* Choose the password length
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
 Password Generator v1.0
==============================

Password length: 12

Generated password:

A7#mQ!2xLp@9

Password saved to passwords.json
```

## Output

Generated passwords are stored in `passwords.json`.

Example:

```json
[
    "A7#mQ!2xLp@9"
]
```

## Technologies

* Python
* secrets
* string
* JSON
