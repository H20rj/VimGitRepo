"""Guessing Game"""

from random import randint


def main() -> None:
    """Main"""
    number = randint(1, 25)
    counter = 0
    user_input: int = 0
    try:
        user_input = int(input("Enter a number 1-25: "))
    except ValueError:
        print("Please enter an integer")
    while user_input != number:
        counter += 1
        if user_input > number:
            print("too high")
            user_input = int(input("Enter a number 1-25: "))
        elif user_input < number:
            print("too low")
            user_input = int(input("Enter a number 1-25: "))
    print(f"Congrats! You got it in {counter} tries!")


if __name__ == "__main__":
    main()
