import sys; sys.stdin = open("27328.txt", "r")

A = int(input())
B = int(input())

if A < B:
    print(-1)
elif A == B:
    print(0)
else:
    print(1)