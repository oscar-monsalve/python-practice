# Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

user_list = []

while True:
    
    try:
        user_input_str = input("Enter a number: ")
        if user_input_str == "done":
            break
        user_int = int(user_input_str)
        user_list.append(user_int)
    except:
        print("Invalid input.")
        continue
     
print(user_list)

min_input = min(user_list)
max_input = max(user_list)
print(f"The minimum and maximum numbers are {min_input} and {max_input}, respectively")