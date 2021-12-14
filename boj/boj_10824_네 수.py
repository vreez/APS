import sys; sys.stdin = open("10824.txt", "r")

A, B, C, D = list(input().split())

first = int(A+B)
second = int(C+D)

print(first + second)