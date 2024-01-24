# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

s = input("Enter any word to check if it's a polindrome: ")
print()

if s[::1] == s[::-1]:
    print(f"{s} is a palindrome word.")
    print()
else:
    print(f"{s} is a palindrome word.")
    print()