"""
Example of tuples
"""
# Comparing tuples: Using sort() to organize from biggest to lowest

# TXT = "but soft what light in yonder window breaks"
# words = TXT.split()
# t = []

# for i in words:
#     t.append((len(i), i))

# t.sort(reverse=True)
# print(t)

# res = []
# for l, w in t:
#     res.append(w)

# print(res)
#_________________________________________________________

# Tuple assignment: Assigning two words with one line of code

# TEXT = "monty@python.org"
# uname, domain = TEXT.split("@")

# print(uname, domain)
#_________________________________________________________

# Dictionaries and tuples

# t = {
#     "a" : 10,
#     "b" : 1,
#     "c" : 22,
# }

# l = list(t.items())
# l.sort()
# print(l)
#_________________________________________________________

# Sorting dictionaries by key and value using tuples

# t = {
#     "c" : 10,
#     "d" : 1,
#     "a" : 22,
#     "b" : 15
# }
#     # Sorting by key
# l = []
# for k, v in list(t.items()):
#     l.append((k, v))
# l.sort()
# print(l)

#     # Soring by value
# l2 = []
# for k, v in list(t.items()):
#     l2.append((v, k))
# l2.sort()
# print(l2)
#_________________________________________________________

# Using tuples as keys in dictionaries

dic = {}
a = (1, 2, 3 ,4)
dic["Monsalve", "Oscar"] = 3154612154

print(dic)
