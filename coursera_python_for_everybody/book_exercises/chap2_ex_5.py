# Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

c_temp = float(input("Enter a Celsius temperature:\n"))

f_temp = (c_temp * 9/5) + 32

print(f"The equivalent temperature in Fahrenheit is:\n {f_temp}")