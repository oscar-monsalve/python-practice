# Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z.

import string

with open("romeo_full.txt", encoding="UTF-8") as text:

    dic = {}
    dic_no_space = {}
    l = []
    for i in text:
        i = i.translate(i.maketrans("", "", string.punctuation))
        i = i.strip().lower()
        for k in i:
            dic[k] = dic.get(k, 0) + 1
        if "\ufeff" in dic:
            del dic["\ufeff"] # Remove the "\ufeff" character

    for k, v in dic.items():
        if k != " " and not k.isnumeric(): # Remove spaces and numbers from the dic dictionary
            dic_no_space[k] = v

    for k, v in list(dic_no_space.items()): # Add the dictionary to an empty list
        l.append((v, k))
    l.sort(reverse=True) # Sort the list by value in descending order

    for k, v in l: # Loop through the list containing tuples and display the key before the value
        print(v, k)
