import re, os

NUMBER_MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

REVERSE_MAPPING = {
    "".join(reversed(key)): value for key, value in NUMBER_MAPPING.items()
}


def get_sum_of_numbers(file_name):
    print(f"USING FILE {file_name}")

    with open(file_name, "r") as file:
        lines = file.readlines()
        numbers = []

        for line in lines:
            char_list = list(line)
            digits = [int(char) for char in char_list if char.isdigit()]
            if len(digits) >= 1:
                first_and_last_number = 10 * digits[0] + digits[-1]
                numbers.append(first_and_last_number)
        print(sum(numbers))


def part_one():
    print("PART ONE: ")
    get_sum_of_numbers("input.txt")


def replace_values(string, replacements):
    def repl(match):
        return replacements[match.group()]

    pattern = r"|".join(replacements.keys())
    return re.sub(pattern, repl, string)


def get_first_numbers(file_name):
    print(f"USING FILE {file_name}")

    with open(file_name, "r") as file:
        lines = file.readlines()
        numbers = []

        for line in lines:
            char_list = list(line)
            digits = [int(char) for char in char_list if char.isdigit()]
            if len(digits) >= 1:
                numbers.append(digits[0])
    return numbers


def part_two():
    print("PART TWO: ")

    with open("input.txt", "r") as file:
        lines = file.read()

    replaced_string = replace_values(lines, NUMBER_MAPPING)

    with open("part_two_output.txt", "w") as output:
        output.write(replaced_string)

    with open("input.txt", "r") as file:
        lines = file.readlines()
    reversed_lines = ""

    for line in lines:
        reversed_line = "".join(reversed(line))
        if not reversed_lines:
            reversed_lines = reversed_line
        else:
            reversed_lines += reversed_line

    replaced_reversed_string = replace_values(reversed_lines, REVERSE_MAPPING)

    with open("part_two_reversed_output.txt", "w") as output:
        output.write(replaced_reversed_string)

    first_numbers = get_first_numbers("part_two_output.txt")

    last_numbers = get_first_numbers("part_two_reversed_output.txt")
    returned_sum = 0
    for i in range(len(first_numbers)):
        returned_sum += 10 * first_numbers[i] + last_numbers[i]

    print("PART TWO RESULT:", returned_sum)


if __name__ == "__main__":
    part_one()
    part_two()
