# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

def chop(t):
    del t[0]
    del t[len(t)-1]
        
def middle(x):
    a = x[1:len(x)-1]
    print(a)
    
    
my_list = ["a", "b", "c", "d"]

# chop(my_list)
# print(my_list)

middle(my_list)

