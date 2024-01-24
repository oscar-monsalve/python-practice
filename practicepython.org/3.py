# Take a list, say for example this one:   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], and write a program that prints out all the elements of the list that are less than 5.

# Extras:

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Ask the user for a number and return a list that contains only elements from the original list "a" that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_than_five = []
user_list = []

print("The numbers less than 5 printed one by one are: ")
for i in a:
    if i < 5:
        print(i)
        less_than_five.append(i) # Extra
print("The numbers less than 5 printed in a list are: ")
print(less_than_five)
print()

# Extra
user_number = int(input("Enter any integer number: "))

for i in a:
    if i < user_number:
        user_list.append(i)
print("The number in the list 'a' that are less than the number you entered are: ")
print(user_list)