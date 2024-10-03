import re

file_name = "actual_data.txt"

with open(file_name, "r") as file:
    numbers = list()
    for i in file:
        lines = i.rstrip()
        x = re.findall("([0-9]+)", lines)
        if len(x) > 0:
            for k in x:
                numbers.append(int(k))

    sum = 0
    for i in numbers:
        sum += i
    print(sum)
