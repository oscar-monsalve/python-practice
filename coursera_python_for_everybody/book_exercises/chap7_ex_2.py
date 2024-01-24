# Write a program to prompt for a file name, and then read through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475.
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.

while True:
    file_name = input("Enter the file name: ")
    try:
        data = open(file_name)
        break
    except:
        print(f"The file name {file_name} does not exists.")

count = 0
sum = 0   
for i in data:
    if i.find("X-DSPAM-Confidence:") == -1:
        continue
    else:
        count += 1
        col_index = i.find(":")
        flt = i[col_index+1:]
        flt_float = float(flt)
        sum += flt_float

aver = sum/count

print(f"The number of DSPAM-Confidence is {count}")
print(f"The average of the DSPAM values is {aver}")
