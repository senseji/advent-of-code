def is_symbol(el):
    if el not in ["."]:
        return True
    return False


def get_lines():
    file_name = "input.txt"

    with open("input.txt", "r") as file:
        lines = file.readlines()

    return lines


def should_skip(line, j):
    if not line[j].isdigit():
        return True
    _j = j - 1
    if _j < 0:
        return False
    if line[_j].isdigit():
        return True
    return False


def find_number(line, j):
    number = ""
    final_index = j

    for _j in range(j, len(line)):
        if line[_j].isdigit():
            number += line[_j]
            final_index = _j
        else:
            break

    return int(number), final_index


def adjacent_to_symbols(massive_array, line_index, start_index, end_index):
    for i in range(line_index - 1, line_index + 2):
        if i < 0 or i >= len(massive_array):
            continue
        for j in range(start_index - 1, end_index + 2):
            if j < 0 or j >= len(massive_array[i]):
                continue
            if i == line_index and j >= start_index and j <= end_index:
                continue
            if is_symbol(massive_array[i][j]):
                return True

    return False


def part_one():
    numbers = []
    lines = get_lines()

    massive_array = [list(line.rstrip("\n")) for line in lines if line.rstrip("\n")]

    for i in range(len(massive_array)):
        for j in range(len(massive_array[i])):
            if should_skip(massive_array[i], j):
                continue
            # get the whole number
            possible_number, _j = find_number(massive_array[i], j)

            if adjacent_to_symbols(massive_array, i, j, _j):
                numbers.append(possible_number)

    print(sum(numbers))


def part_two():
    pass


if __name__ == "__main__":
    part_one()
    part_two()
