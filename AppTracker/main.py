from library import view_status, change_status


def main():
    print("What would you like to do?")
    print("    1. View Status")
    print("    2. Change Status")
    print("    3. Exit")
    user_input = input("Enter here: ")
    print()
    if user_input == "1":
        view_status()
    elif user_input == "2":
        change_status()
    elif user_input == "3":
        exit(1)


if __name__ == "__main__":
    main()
