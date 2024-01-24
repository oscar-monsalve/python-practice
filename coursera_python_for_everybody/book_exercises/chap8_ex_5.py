# Write a program to read through the mail box data and when you find line that starts with “From”, you will split the line into words using the split function. We are interested in who sent the message, which is the second word on the From line.

# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# You will parse the From line and print out the second word for each From line, then you will also count the number of From (not From:) lines and print out a count at the end.

text = open("mbox_short.txt", "r")

count = 0

for i in text:
    lines = i.split()
    if len(lines) == 0 or lines[0] != "From":
        continue
    else:
        print(lines[1])
    
    count += 1
    
print(f"There were {count} lines in the file with From as the first word")