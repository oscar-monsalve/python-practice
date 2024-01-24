# Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

text = open("mbox_short.txt", "r")

dic = {}
# LARGEST = 0 # For max() function
BIGNUMBER = None
BIGWORD = None

for i in text:
    i = i.split()
    if len(i) == 0 or i[0] != "From":
        continue
    i = i[1]
    dic[i] = dic.get(i, 0) + 1

for k, v in dic.items():
    if BIGNUMBER is None or v > BIGNUMBER:
        BIGNUMBER = v
        BIGWORD = k

print(f"The person {BIGWORD} has sent the most amount of emails: {BIGNUMBER}")

#     # Checking the maximum occurrence to check with the max function
#     if LARGEST < dic[i]:
#         LARGEST = dic[i]

# print(f"{max(dic)} has sent the largest number of emails: {LARGEST}")
text.close()
