a = [2, 3, 5, 3, 9, 20, 35, 14, 40, 31]
seen = None

for i in a:
    if seen is None:
        seen = i
    elif i > seen:
        seen = i

print("The largest is:", seen)           