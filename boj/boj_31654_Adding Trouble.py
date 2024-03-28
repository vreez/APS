import sys; sys.stdin = open("31654.txt", "r")

A, B, C = map(int, input().split())
if A + B == C:
    print("correct!")
else:
    print("wrong!")