# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

import random
ran = random.randint(0, 9999)
ran_str = f"{ran:04d}" # Formated to include the 0000 combination and a 4-digit number
# ran_int = int(ran_str)
print(f"The generated random number is: {ran_str}\n")

GUESS_COUNT = 0
while True:
    l_ran = []
    l_guess = []

    while True:
        try:
            guess = input("Enter a 4-digit number (or \"done\" to finish): ")
            if guess == "done":
                break
            guess_int = int(guess)
            if len(guess) != 4:
                print("Error. Ensure the number has 4 digits.")
                continue
            break
        except ValueError:
            print("Invalid input.")

    for i in str(guess):
        l_guess.append(i)
    for i in ran_str:
        l_ran.append(i)

    COUNT_COWS = 0
    COUNT_BULLS = 0
    for i in range(4):
        if l_guess[i] == l_ran[i]:
            COUNT_COWS += 1
        elif l_guess[i] in l_ran:
            COUNT_BULLS += 1

    GUESS_COUNT += 1
    if guess != ran_str:
        print(f"cows: {COUNT_COWS}, bulls: {COUNT_BULLS}")
    elif guess == ran_str:
        print(f"You guessed the number! It took {GUESS_COUNT} guesses.")
        break
