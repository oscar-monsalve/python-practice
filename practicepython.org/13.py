# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fib_gen(input, init=1, f_prev=0, f_new=0):
    fib = []
    for i in range(input):
        f_new = init + f_prev
        init = f_prev
        f_prev = f_new
        fib.append(f_new)
    print(f"The list of Fibonacci numbers is: {fib}")
    

while True:
    try:
        input = int(input("Enter a number to generate as many Fibonacci numbers: "))
        break
    except:
        print("Invalid input")

fib_gen(input)
