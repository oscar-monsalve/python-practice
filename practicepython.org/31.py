"""
Write a function that picks a random word from a list of words from the SOWPODS dictionary
"""

import random

def generate_word():
    """ This function chooses a random word from a dictionary"""

    rand = random.randint(1, 267751) # 267751 is the number of words in the .txt file

    list_words = []
    with open("word_dictionary.txt", "r", encoding="UTF-8") as words:
        for i in words:
            i = i.rstrip().lower()
            list_words.append(i)

    chosen_word = list_words[rand]

    chosen_word_list = []
    for i in chosen_word:
        chosen_word_list.append(i)

    print(f"The chosen word is: {chosen_word}")

generate_word()
