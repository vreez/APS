import sys; sys.stdin = open("27332.txt", "r")

A = int(input())
B = int(input())

if A + (B * 7) <= 30:
    print(1)
else:
    print(0)