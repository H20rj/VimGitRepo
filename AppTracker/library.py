# from os.path import exists
from typing import Dict


def load_status() -> Dict[str, str]:
    db_dict: Dict[str, str] = {}
    with open("saves/status.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            split_status = line.split(":")
            db_dict[split_status[0].strip()] = split_status[1].strip()
        return db_dict


def change_status() -> None:
    db_dict = load_status()
    print("What school would you like to change?:")
    print("    1. OU")
    print("    2. CSU")
    print("    3. CU")
    print("    4. Texas Tech")
    print("    5. Trinity")
    print("    6. Mines")
    print("    7. DU")
    user_input = input("Enter here: ")
    school = ""
    while user_input not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid Input")
        user_input = input("Try again, enter here:")
    if user_input == "1":
        school = "OU"
    elif user_input == "2":
        school = "CSU"
    elif user_input == "3":
        school = "CU"
    elif user_input == "4":
        school = "Texas Tech"
    elif user_input == "5":
        school = "Trinity"
    elif user_input == "6":
        school = "Mines"
    elif user_input == "7":
        school = "DU"
    print("New status:")
    print("    1. Accepted")
    print("    2. Denied")
    print("    3. Pending")
    user_input = input("Enter here: ")
    new_status = ""
    while user_input not in ["1", "2", "3"]:
        print("Invalid Input")
        user_input = input("Enter here: ")
    if user_input == "1":
        new_status = "Accepted"
    elif user_input == "2":
        new_status = "Denied"
    elif user_input == "3":
        new_status = "Pending"
    db_dict[school] = new_status

    def save_status() -> None:
        iterations = 0
        db_dict_keys: list[str] = list(db_dict.keys())
        with open("saves/status.txt", "w") as f:
            for i in db_dict:
                f.write(f"{db_dict_keys[iterations]}: {db_dict[i]}\n")
                iterations += 1

    save_status()


def view_status() -> None:
    db_dict = load_status()
    iterations = 0
    db_dict_keys: list[str] = list(db_dict.keys())
    for i in db_dict:
        print(f"{db_dict_keys[iterations]}: {db_dict[i]}")
        iterations += 1
