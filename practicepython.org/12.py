# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

new_list = [5, 10, 15, 20, 25]


def picker(new_list):
    return [new_list[0], new_list[len(new_list)-1]]

print(picker(new_list))