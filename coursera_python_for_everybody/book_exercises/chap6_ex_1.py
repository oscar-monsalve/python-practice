# Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

# Solution using a while loop
fruit = "banana"
length = len(fruit)

index = 0
while index < length:
    letter = fruit[index]
    print(letter, index, length)
    index += 1


# Solution using a for loop
for i in fruit:
    print(i)