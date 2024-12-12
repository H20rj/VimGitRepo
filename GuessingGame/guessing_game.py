"""Guessing Game"""

from random import randint


def main() -> None:
    """Main"""
    number = randint(1, 25)

    user_input = int(input("Enter a number 1-25: "))
    while user_input != number:
        if user_input > number:
            print("too high")
            user_input = int(input("Enter a number 1-25: "))
        elif user_input < number:
            print("too low")
            user_input = int(input("Enter a number 1-25: "))
        elif user_input == number:
            print("You got it!")


if __name__ == "__main__":
    main()
