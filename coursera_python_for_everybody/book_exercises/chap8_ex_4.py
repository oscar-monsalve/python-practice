# Create a list of unique words, which will contain the final result. Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function. For each word, check to see if the word is already in the list of unique words. If the word is not in the list of unique words, add it to the list. When the program completes, sort and print the list of unique words in alphabetical order.

text = open("romeo.txt", "r")

all_words = []
unique = []

for i in text:
    i = i.rstrip()
    i = i.split(" ")
    all_words.append(i)

all_words_flatten = sum(all_words, [])

for i in all_words_flatten:
    if i not in unique:
        unique.append(i)

unique.sort()
print(unique)