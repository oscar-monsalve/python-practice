# Exercise 1: Write a simple program to simulate the operation of the grep com-
# mand on Unix. Ask the user to enter a regular expression and count the number
# of lines that matched the regular expression:
#
# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author
#
# $ python grep.py
# Enter a regular expression: ^X-
# mbox.txt had 14368 lines that matched ^X-
#
# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4175 lines that matched java$

import re

file_path = "mbox.txt"

with open(file_path, "r") as file:
    user_input = input("Enter a regular expression: ")

    sum = 0
    for i in file:
        line = i.rstrip()
        if re.search(user_input, line):
            sum += 1

    print(f"The file \"{file_path}\" had {sum} lines that matched \"{user_input}\"")
