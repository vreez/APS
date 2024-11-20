import sys; sys.stdin = open("523.txt", "r")

a, b = map(int, input().split())

if a > b:
    print("{} > {} --- 1".format(a, b))
else:
    print("{} > {} --- 0".format(a, b))
if a < b:
    print("{} < {} --- 1".format(a, b))
else:
    print("{} < {} --- 0".format(a, b))
if a >= b:
    print("{} >= {} --- 1".format(a, b))
else:
    print("{} >= {} --- 0".format(a, b))
if a <= b:
    print("{} <= {} --- 1".format(a, b))
else:
    print("{} <= {} --- 0".format(a, b))