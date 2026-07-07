from password_generator import generate_password, save_password


def main():

    print("==============================")
    print(" Password Generator v1.0")
    print("==============================")

    length = int(input("\nPassword length: "))

    password = generate_password(length)

    print("\nGenerated password:\n")
    print(password)

    save_password(password)

    print("\nPassword saved to passwords.json")


if __name__ == "__main__":
    main()