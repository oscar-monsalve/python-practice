# Dictionaries

# Create an empty dictionary and add a key using [] and a value after =
# eng2sp = dict()
# eng2sp["one"] = "uno"
# print(eng2sp)
# _____________________________________________________________________________________

# Create a dictionary adding keys and values manually using {}

# eng2sp = {
#     "one" : "uno",
#     "two" : "dos",
#     "three" : "tres"
# }

# # _____________________________________________________________________________________

# # The "in" operator checks if a certain KEY exists in the dictionary, not the value.
# print("uno" in eng2sp)

# # To see whether something appears as a value in a dictionary, you can use the method values, which returns the values as a type that can be converted to a list, and then use the in operator:

# print("dos" in list(eng2sp.values()))
# # _____________________________________________________________________________________


# Count how many time a letters repeats in a string
    # Method 1. For loop and count manually

# word = "Oscar Dario Monsalve Cifuentes"
# dic = {}
# for i in word:
#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i] += 1

# print(dic)

    # Method 2. Using a for loop and the function get()
    
word = "Oscar Dario Monsalve Cifuentes"
dic = {}
for i in word:
    dic[i] = dic.get(i,0) + 1    

print(dic)