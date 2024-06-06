import sys; sys.stdin = open("31922.txt", "r")

A, P, C = map(int, input().split())

if P > A + C:
    print(P)
else:
    print(A+C)