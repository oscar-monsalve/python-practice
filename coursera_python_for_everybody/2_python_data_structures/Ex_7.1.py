# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.

file_name = input("Enter the file name: ")
data = open(file_name, "r")

for i in data:
     i = i.upper().rstrip()
     print(i)