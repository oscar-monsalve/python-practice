# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and at the end prints out both the maximum and minimum of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.


count = 0
total = 0
list = []
smallest = None
largest = None

while True:   
    try:        
        number_input = input("Enter any number: ")
        if number_input == "done":
            print("The program has ended.\n")
            break
        else:
            number_input = int(number_input)
            list.append(number_input)
            count += 1
            
    except:
        print("Invalid input")

for i in list:
    total += i
    if smallest is None or i < smallest:
        smallest = i
    elif largest is None or i > largest:
        largest = i
    
    

average = total/count
print(f"The count is {count}")
print(f"The total sum is {total}")
print(f"The minimum is {smallest}")
print(f"The maximum is {largest}")