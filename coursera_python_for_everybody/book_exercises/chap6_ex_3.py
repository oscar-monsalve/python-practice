# Exercise 3: Write a function named count that takes the arguements of a string and a letter to determine how many time a certain word appears in the string

def count(string, letter):
    count = 0
    list = []
    for i in string:
        if i == letter:
           count += 1
           list.append(count)
    print(f"The number of times the letter \"{letter}\" appers in the word \"{string}\" is: {len(list)}")
       
string = "Oscar Dario Monsalve Cifuentes"
letter = "a"

count(string,letter)
    