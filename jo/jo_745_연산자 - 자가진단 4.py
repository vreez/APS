import sys; sys.stdin = open("745.txt", "r")

a = int(input())
b = int(input())

if a > b:
    print("{} > {} --- {}".format(a, b, True))
else:
    print("{} > {} --- {}".format(a, b, False))

if a < b:
    print("{} < {} --- {}".format(a, b, True))
else:
    print("{} < {} --- {}".format(a, b, False))

if a >= b:
    print("{} >= {} --- {}".format(a, b, True))
else:
    print("{} >= {} --- {}".format(a, b, False))

if a <= b:
    print("{} <= {} --- {}".format(a, b, True))
else:
    print("{} <= {} --- {}".format(a, b, False))