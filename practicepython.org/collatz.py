# Take any positive integer n. If n is even, divide n by 2 to get n / 2. If n is odd, multiply n by 3 and add 1 to get 3n + 1. Repeat the process indefinitely. The conjecture states that no matter which number you start with, you will always reach 1 eventually. Given a number n, return the number of steps required to reach 1.

import numpy as np
import matplotlib.pyplot as plt

y = []

while True:
    count = 0
    
    try:
        n = int(input("Enter an integer number: "))
        x = n
        break
    except:
        print("Invalid input.")

while True:
    if n == 1:
        print(f"The program has ended with a value of {n}\n")
        break
    elif n % 2 == 0:
        n = n/2
    elif n % 2 != 0:
        n = n*3+1
    
    count += 1
    y.append(n)
    # print(n)


print(f"It took {count} cycles to reach {n}")
x = np.arange(1, len(y)+1, 1)

plt.plot(x,y)
plt.show()

  