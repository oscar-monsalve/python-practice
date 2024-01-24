# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

repeat = True
count = 0

while repeat:
    
    count += 1
    random_gen = random.randint(1, 9)
    user_guess = int(input("The computer has chosen randomly a number from 1 to 9. Try to guess it: "))
    
    if user_guess < random_gen:
        print("The guess is too low")
    elif user_guess > random_gen:
        print("The guess is too high")
    else:
        print(f"You have guessed correctly the number in {count} tries.")
       
    exit = input("If you want to keep guessing, type 'y'. If not type 'exit': ")
    
    if exit == "exit":
        break
    if exit == "y":
        continue