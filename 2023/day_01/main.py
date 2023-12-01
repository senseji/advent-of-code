NUMBER_MAPPING = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}


def part_one(file_name):
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


def part_two():
    with open("input.txt", "r") as input:
        raw_file = input.read()

    for key, value in NUMBER_MAPPING.items():
        raw_file = raw_file.replace(key, str(value))

    with open("part_two_output.txt", "w") as output:
        output.write(raw_file)

    print("PART TWO: ")

    part_one("part_two_output.txt")


if __name__ == "__main__":
    part_one("input.txt")
    part_two()
