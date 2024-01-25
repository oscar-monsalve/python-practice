a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

lst = []

if len(a) != len(b):
    if len(a) < len(b):
        a.append([(len(b)-len(a))] * 0)

print(type(len(a)))
