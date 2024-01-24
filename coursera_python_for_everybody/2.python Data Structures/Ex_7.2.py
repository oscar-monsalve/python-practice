# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.


file_name = input("Enter the file name: ")
data = open(file_name)

count = 0
added = 0   
for i in data:
    if i.find("X-DSPAM-Confidence:") == -1:
        continue
    else:
        count += 1
        col_index = i.find(":")
        flt_str = i[col_index+1:]
        flt_float = float(flt_str)
        added += flt_float

aver = added/count

print(f"Average spam confidence: {aver}")