# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).

#Extras:
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button).

name = input("What is your name? ")
age = int(input(name + ", what is your current age? "))
current_year = 2023

age_100 = current_year + (100-age)

print(name + ", you will turn 100 years old in the year " + str(age_100))

number = float(print("Ok, now write a random number: "))