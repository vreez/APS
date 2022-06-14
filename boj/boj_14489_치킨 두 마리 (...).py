import sys; sys.stdin = open("14489.txt", "r")

A, B = map(int, input().split())
chicken = int(input())

if A + B >= chicken * 2:
    print(A + B - (chicken * 2))
else:
    print(A + B)
