n = float(input())

if n <= 50.80:
    print("Flyweight")
elif n <= 61.23:
    print("Lightweight")
elif n <= 72.57:
    print("Middleweight")
elif n <= 88.45:
    print("Cruiserweight")
else:
    print("Heavyweight")