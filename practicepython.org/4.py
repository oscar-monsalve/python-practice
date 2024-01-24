# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

number = int(input("Enter an integer number: "))
print()

list_1 = list(range(1, number + 1))
list_2 = []

for i in list_1:
    if number % i == 0:
        list_2.append(i)

print(f"The numbers that divide completely {number} are: ")        
print(list_2)
print()