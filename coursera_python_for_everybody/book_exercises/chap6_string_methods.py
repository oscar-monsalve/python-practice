# Write an invocation that counts the number of times the letter a occurs in “banana”.

str = "banana"
result = str.count("a")
print(result)

# Print out only the second half of the address:"From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"  Ex.: (i.e., uct.ac.za)

data =  "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

# First, find the posistion of "@"
at_pos = data.find("@")

# Second, find the index position of the space after ".za"
sp_pos = data.find(" ", at_pos)
print(sp_pos)

# Third, obtain the strings between the above indexes
result = data[at_pos+1:sp_pos]
print(result)



# String formating

years = 2
camels = 0.1
animal = "camels"

print("In %d years I've spotted %g %s" %(years, camels, animal))