x, y = map(float, input().split())

if x >= 4.0 and y >= 4.0:
    print("A grade")
elif x >= 3.0 and y >= 3.0:
    print("B grade")
else:
    print("F grade")