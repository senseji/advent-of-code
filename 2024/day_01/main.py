with open("input.txt", "r") as file:
    lines = file.readlines()

first, last = [], []
for line in lines:

    splittext = line.split(" ")
    first.append(int(splittext[0]))
    last.append(int(splittext[-1]))

# Part 1
first = sorted(first)
last = sorted(last)

sum_of_differences = 0
for f, l in zip(first, last):
    sum_of_differences += abs(l - f)
print(sum_of_differences)

# Part 2
occurences = {el: 0 for el in first}

for el in last:
    if el in occurences:
        occurences[el] += 1

sum_of_occurences = 0
for key, value in occurences.items():
    sum_of_occurences += key * value
print(sum_of_occurences)
