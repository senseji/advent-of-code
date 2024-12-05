with open("./input.txt", "r") as file:
    lines = file.readlines()

safe_reports = 0


def is_ok(cur, next, asc):
    if asc and cur > next:
        return False
    elif not asc and cur < next:
        return False
    elif abs(cur - next) > 3 or abs(cur - next) == 0:
        return False
    return True


# Part 1
for line in lines:
    numbers = list(map(int, line.split(" ")))

    if numbers[0] < numbers[1]:
        asc = True
    else:
        asc = False

    for i in range(len(numbers) - 1):
        if not is_ok(numbers[i], numbers[i + 1], asc):
            break
    else:
        safe_reports += 1


print(safe_reports)
safe_reports = 0

# Part 2
# we need to check if all the numbers are in ascending or descending order, and that the difference between them is less than or equal 3 (part1).
# Part2 is that we will try to remove one number from the list and check if the list is still valid.

found = False

for line in lines:

    modified_line = line.split(" ")
    original_numbers = list(map(int, modified_line))

    found = False

    for i in range(len(original_numbers)):
        numbers = original_numbers.copy()

        numbers.pop(i)

        if numbers[0] < numbers[1]:
            asc = True
        else:
            asc = False

        for i in range(len(numbers) - 1):
            if not is_ok(numbers[i], numbers[i + 1], asc):
                break
        else:
            safe_reports += 1
            found = True
            break

print(safe_reports)
