# Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary. After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# text = open("mbox_short.txt", "r", encoding="UTF-8")
with open("mbox_short.txt", encoding="UTF-8") as text:
    dic = {}
    l = []

    for i in text:
        i = i.split()
        if len(i) == 0 or i[0] != "From":
            continue
        i = i[1]
        dic[i] = dic.get(i, 0) + 1

        # Creating list of tuples
        for k, v in list(dic.items()):
            l.append((v, k))

    l.sort(reverse=True)

    # Used tuple assigment to assign max occurrence (NUMBER) and the NAME to print it in the order of NAME, NUMBER. Otherwise, it would print viceversa
    NUMBER, NAME = l[0]

    print(NAME, NUMBER)
