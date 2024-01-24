# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

text = open("mbox_short.txt", "r")

dic = {}
for i in text:
    i = i.split()
    if len(i) == 0 or i[0] != "From":
        continue
    i = i[1]
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

print(dic)
