import sys; sys.stdin = open("13623.txt", "r")

A, B, C = map(int, input().split())

if A == B and B == C:
    print("*")
elif A == B and B != C:
    print("C")
elif A != B and B == C:
    print("A")
else:
    print("B")