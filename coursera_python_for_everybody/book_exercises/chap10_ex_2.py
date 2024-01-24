# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.
# Sample line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

with open("mbox_short.txt", encoding="UTF-8") as text:

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
                     