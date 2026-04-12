X, Y = map(float, input().split())

if X >= 4.0 and Y >= 4.0:
    print("A grade")
elif X >= 3.0 and Y >= 3.0:
    print("B grade")
else:
    print("F grade")