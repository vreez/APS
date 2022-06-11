import sys; sys.stdin = open("25238.txt", "r")

A, B = map(int, input().split())

de = A*((100 - B)/100)

if de >= 100:
    print(0)
else:
    print(1)