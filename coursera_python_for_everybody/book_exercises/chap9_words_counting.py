# write a Python program to read through the lines of the file, break each line into a list of words, and then loop through each of the words in the line and count each word using a dictionary.add()

while True:
    try:
        user_input = input("Enter the text file to read: ")
        text = open(user_input, "r")
        break
    except ValueError:
        print("The file name does not exists.")
        continue

count = {}

for i in text:
    i = i.rstrip().split()
    for k in i:
        if k not in count:
            count[k] = 1
        else:
            count[k] += 1

print(count)