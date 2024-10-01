# Exercise 2: Write a program to look for lines of the form:
#
# New Revision: 39772
#
# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers and
# print out the average as an integer.


import re

with open("mbox-short.txt", "r") as file:
    numbers = list()
    for i in file:
        i = i.rstrip()
        x = re.findall("New Revision: ([0-9]+)", i)
        if len(x) > 0:
            numbers.append(x)

    sum = 0
    for i in numbers:
        print(i)

    # print(sum)
    # num_average = sum / len(numbers)
