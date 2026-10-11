a, b = map(int, input().split())

if a >= 3 and b >= 3:
    print("High")
elif a >= 3 or b >= 3:
    print("Mid")
else:
    print("Low")