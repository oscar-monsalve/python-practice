score = float(input("What's the score? "))

if score > 1:
    print("Error. The score is out of range")
    quit()
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
elif score < 0.6:
    print("F")