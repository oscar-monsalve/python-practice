"""
Write a code to count the occurence of words in a text file and print the ten most common words. Remember to handle the punctuation signs and upper case letters
"""

import string

text = open("romeo_punct.txt", encoding="UTF-8")

dic = {}
for i in text:
    i = i.translate(str.maketrans("", "", string.punctuation))
    i = i.lower()
    i = i.split()
    for k in i:
        dic[k] = dic.get(k, 0) + 1

# Sort the dictionary by value
l = list((dic.items()))
l2 = []

for k, v in l:
    l2.append((v, k))

l2.sort(reverse=True)

# Print only the first 10 words
print("The 10 most common words are: \n")
for k, v in l2[:10]:
    print(k, v)
   