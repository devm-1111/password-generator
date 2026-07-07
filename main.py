from password_generator import generate_password, save_password


def ask(question):
    return input(question).lower() == "y"


def main():

    print("==============================")
    print(" Password Generator v1.1")
    print("==============================")

    length = int(input("\nPassword length: "))

    uppercase = ask("Include uppercase letters? (y/n): ")
    lowercase = ask("Include lowercase letters? (y/n): ")
    numbers = ask("Include numbers? (y/n): ")
    symbols = ask("Include symbols? (y/n): ")

    password = generate_password(
        length,
        uppercase,
        lowercase,
        numbers,
        symbols
    )

    if password is None:
        print("\nError: Select at least one character type.")
        return

    print("\nGenerated password:\n")
    print(password)

    save_password(password)

    print("\nPassword saved to passwords.json")


if __name__ == "__main__":
    main()