# Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program. Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”. The program should behave normally for all other files which exist and don’t exist.

while True:
    file_name = input("Enter the file name: ")
    if file_name == "na na boo boo":
            print("NA NA BOO BOO TO YOU - You've benn punk'd!")
            continue
    try:
        data = open(file_name)
        break
    except:
        print(f"The file name {file_name} does not exists.")

count = 0
for i in data:
    count += 1
    
print(f"The number of lines in the file {file_name} is: {count}")
