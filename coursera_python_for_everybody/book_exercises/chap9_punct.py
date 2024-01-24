# Read a file with punctuation and get rid of it. Additionally, print the number of words collected within a dictionary.

import string

while True:
    try:
        user_input = input("Enter the file name to read: ")
        if user_input == "done":
            print("The program ended")
            break
        text = open(user_input, "r")
        break
    except ValueError:
        print("Invalid input.")
        continue

dic = {}
for i in text:
    i = i.translate(i.maketrans("", "", string.punctuation))
    i = i.rstrip().lower().split()
    for k in i:
        if k not in dic:
            dic[k] = 1
        else:
            dic[k] = dic.get(k, 0) + 1

print(dic)
