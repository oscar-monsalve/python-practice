# Exercise 5: Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

str = "X-DSPAM-Confidence:0.8475"

col_pos = str.find(":")
extract = str[col_pos+1:]
flt = float(extract)


print("The extracted number is: %g" %flt)
print("The type of the number is: ", type(flt))