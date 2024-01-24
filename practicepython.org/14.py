# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.


# Solution 1: using sets

def no_duplicates_with_sets(x):
    a = list(set(x))
    print(f"The list without duplicates using sets is: \n {a}")
    return a
    

# Solution 2: using lists and a for loop

def no_duplicates_with_loop(x):
    list_solution_2 = []
    for i in x:
        if i not in list_solution_2:
            list_solution_2.append(i)
    print(f"The list without duplicates using lists and for loop is: \n {list_solution_2}")
    return list_solution_2


test_list = [1, 1, 2, 8, 9, 1, 10, 12, 15, 15, 20, 21, 22, 23, 23, 25, 25, 30]

no_duplicates_with_sets(test_list)

no_duplicates_with_loop(test_list)
