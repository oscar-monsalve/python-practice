# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock


while True:
    p_1 = input("Player 1, what is your play (rock/paper/scissors)? ")
    p_2 = input("Player 2, what is your play (rock/paper/scissors)? ")
    print()

    if p_1 == p_2:
        print("It's a tie.")
    elif p_1 == "rock":
        if p_2 == "scissors":
            print("Player 1 wins.")
            print()
        else:
            print("Player 2 wins.")
            print()
    elif p_1 == "paper":
        if p_2 == "rock":
            print("Player 1 wins.")
            print()
        else:
            print("Player 2 wins.")
            print()
    elif p_1 == "scissors":
        if p_2 == "paper":
            print("Player 1 wins")
            print()
        else:
            print("Player 2 wins.")
            print()
    repeat = input("If you want to play again, type 'y': ")
    if repeat.lower() != "y":
        break
