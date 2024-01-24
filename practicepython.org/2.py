# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = int(input("Enter any integer number: "))

test = number % 2

if test > 0:
    print("The number you entered is odd.")
else:
    print("The number you entered is even.")
    
multiple_4 = number % 4

if multiple_4 == 0:
    print("The entered number is a mutiple of 4.")
    
num = int(input("Enter other integer number to check if it's even or odd: "))
num_check = int(input("Next, enter an integer number to divide the previous number: "))

mod_check = num % num_check 

if mod_check > 0:
    print("The number does not divide evenly, then the result it's odd")
else:
    print("The number divides evenly, then it's even")
