import os

from password_generator import (
    generate_password,
    save_password,
    load_passwords,
    clear_passwords
)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def ask(question):
    return input(question).lower() == "y"


def generate():

    print("==============================")
    print(" Generate Password")
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


def view_passwords():

    passwords = load_passwords()

    if not passwords:
        print("\nNo saved passwords.")
        return

    print("==============================")
    print(" Saved Passwords")
    print("==============================\n")

    for i, password in enumerate(passwords, start=1):
        print(f"{i}. {password}")


def delete_passwords():

    passwords = load_passwords()

    if not passwords:
        print("\nNo saved passwords.")
        return

    answer = input(
        "\nAre you sure you want to clear the password history? (y/n): "
    ).lower()

    if answer == "y":
        clear_passwords()
        print("\nPassword history cleared.")
    else:
        print("\nOperation cancelled.")


def menu():

    while True:

        clear_screen()

        print("==============================")
        print(" Password Generator v1.2")
        print("==============================")
        print("1. Generate password")
        print("2. View saved passwords")
        print("3. Clear password history")
        print("4. Exit")

        option = input("\nSelect an option: ")

        clear_screen()

        if option == "1":
            generate()
            pause()

        elif option == "2":
            view_passwords()
            pause()

        elif option == "3":
            delete_passwords()
            pause()

        elif option == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")
            pause()


if __name__ == "__main__":
    menu()