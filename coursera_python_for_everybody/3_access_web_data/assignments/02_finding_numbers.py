import re

file_name = "sample.txt"

with open(file_name, "r") as file:
    numbers = list()
    for i in file:
        lines = i.rstrip()
        x = re.findall(r"([0-9]+)", lines)
        if len(x) > 0:
            numbers.append(x)

    print(numbers)
