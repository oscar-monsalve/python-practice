# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

text = open("mbox-short.txt")

dic = {}
l = []
for i in text:
    i = i.split()
    if len(i) == 0 or i[0] != "From":
        continue
    i = i[5].split(":")
    i = i[0]
    dic[i] = dic.get(i, 0) + 1

for k, v in list(dic.items()):
    l.append((k, v))

l.sort()

for k, v in l:
    print(k, v)
