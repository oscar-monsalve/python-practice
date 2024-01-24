# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. 

# For example, say I type the string:
#   My name is Michele
# Then I would see the string:
#   Michele is name My

def reverse_string():
    x = input("Enter a long string: ")
    result = x.split()
    result_2 = result[::-1]
    result_3 = ' '.join(result_2)
    return print(f"The reverse order of words are: \n {result_3}")

reverse_string()