import sys; sys.stdin = open("14470.txt", "r")

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if A < 0:
    print(((0 - A) * C) + D + (B * E))
elif A == 0:
    print(D + (B * E))
else:
    print((B - A) * E)