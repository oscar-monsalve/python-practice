# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

text = open("mbox_short.txt", "r")

dic = {}
for i in text:
    i = i.split()
    if len(i) == 0 or i[0] != "From":
        continue
    i = i[2]
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

print(dic)
