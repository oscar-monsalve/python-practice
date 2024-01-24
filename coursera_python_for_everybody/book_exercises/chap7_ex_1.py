# Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case. Handle the error that might cause a wrong file name

while True:
    user_input = input("Enter the file name: ")
    try:
        data = open(user_input)
        break
    except:
        print(f"The file name {user_input} does not exists.")

for i in data:
    i = i.upper()
    print(i)