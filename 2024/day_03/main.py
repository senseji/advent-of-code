import re


with open("input.txt", "r") as file:
    file_str = file.read()

file_str = file_str.replace("\n", "")


# Part 1

expected_pattern = r"mul\(\d+,\d+\)"
matches = re.findall(expected_pattern, file_str)

sum_of_muls = 0
for match in matches:
    a, b = map(int, match[4:-1].split(","))
    sum_of_muls += a * b

print(sum_of_muls)

# Part 2

do_pattern = r"do\(\)"
dont_pattern = r"don\'t\(\)"

do_matches_indices = [m.start() for m in re.finditer(do_pattern, file_str)]
dont_matches_indices = [m.start() for m in re.finditer(dont_pattern, file_str)]
mul_matches_indices = [m.start() for m in re.finditer(expected_pattern, file_str)]

sum_of_muls = 0

indices = {}
for i in do_matches_indices:
    indices[i] = "do"
for i in dont_matches_indices:
    indices[i] = "dont"
for i in mul_matches_indices:
    indices[i] = "mul"

do = True

for i in sorted(indices.keys()):
    if indices[i] == "do":
        do = True
    elif indices[i] == "dont":
        do = False
    elif indices[i] == "mul" and do:

        match = re.search(expected_pattern, file_str[i:])
        a, b = map(int, match.group()[4:-1].split(","))
        sum_of_muls += a * b


print(sum_of_muls)
