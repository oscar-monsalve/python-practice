# Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary

text = open("words.txt", "r")

user_dict = {}

for i in text:
    i = i.strip().split()
    for k in i:
        user_dict[k] = 1
    
print(user_dict)
print("for" in user_dict)
    