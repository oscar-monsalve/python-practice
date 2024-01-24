# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.


COUNT = 0
TOTAL = 0
list = []

while True:   
    try:        
        number_input = input("Enter any number: ")
        if number_input == "done":
            print("The program has ended.\n")
            break
        else:
            number_input = int(number_input)
            list.append(number_input)
            COUNT += 1
            
    except:
        print("Invalid input")

for i in list:
    TOTAL += i

average = TOTAL/COUNT
print(f"The count is {COUNT}")
print(f"The total sum is {TOTAL}")
print(f"The average is {average}")