# Write a program in which the user can type which file to open. Manage the error of a non-existent file with try and except. Count how many lines start with "Subject:".

while True:
    try:
        name = input("Enter the file name to open: ")
        data = open(name)
        break
    except:
        print(f"The file {name} does not exist. Please ensure the file exists.\n")

count = 0
for i in data:
    if i.startswith("Subject:") == -1:
        continue
    else:
        count += 1

print(f"The file {name} has {count} lines starting with \"Subject:\"")

    
