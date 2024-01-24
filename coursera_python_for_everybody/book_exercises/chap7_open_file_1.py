data = open("mbox_short.txt")

# Counting the number of lines in a file

# count = 0
# for i in data:
#     count += 1
# print(f"The number of lines is: {count}\n")
    
    
# Counting the number of characters in a file
inp = data.read()
inp_count = len(inp)
print(f"The number of characters is: {inp_count}")