"""Takes a string and formats in to answers"""


def answer_format(string="ABCD ABCD") -> str:
    """Format"""
    string = string.replace(" ", "")
    output = ""
    iterations = 0
    for letter in string:
        iterations += 1
        temp_put = f"{iterations}: {letter}\n"
        output = output + temp_put
    return output


def main() -> None:
    user_string = input("Please enter a string of answers Ex: ABCD ABD:\n")
    print(answer_format(user_string))


if __name__ == "__main__":
    main()
