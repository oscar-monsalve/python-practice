# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions.


number = int(input("Enter any integer number: "))

list = list(range(1, number+1))
a = [] 

if number < 2 :
        print(f"{number} is not a prime number")

for i in list:
    if number % i == 0:
        a.append(i)

if len(a) > 2:
    print(f"{number} is not a prime number")
elif len(a) == 2:
    print(f"{number} is a prime number")
    

# For some reason, the logic of this exercise was very difficult for me.