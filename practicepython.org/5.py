# Take two lists, and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python


import random

a = random.sample(range(100), 10)
b = random.sample(range(100), 13)

print(a, b)

common_list = []

for i in a:
    if i in b:
        common_list.append(i)
        
print("The numbers that are common between lists 'a' and 'b' are: ")
print()
print(set(common_list)) 
print()