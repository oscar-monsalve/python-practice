# Count the lines starting with "From:" and removing the white spaces

# data = open("mbox_short.txt")

# count = 0
# for i in data:
#     i = i.rstrip()
#     if i.startswith("From:"):
#         count += 1
#         # print(i)
# print(f"The number of lines starting with \"From:\" is: {count}")


# Print the lines that have only "@uct.ac.za" skipping the lines that don't have the "@uct.ac.za" string

data = open("mbox_short.txt")

for i in data:
    i = i.rstrip()
    if i.find("@uct.ac.za") == -1 :
        continue
    else:
        print(i)