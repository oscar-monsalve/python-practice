# This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

text = open("mbox_short.txt", "r")

dic = {}

for i in text:
    i = i.rstrip()
    if i.startswith("From "):
        at_pos = i.find("@")
        day_pos = i.find(" ", at_pos)
        domain = i[at_pos + 1:day_pos]
        if domain not in dic:
            dic[domain] = 1
        else:
            dic[domain] += 1

print(dic)
