import sys; sys.stdin = open("1849.txt", "r")

A, M = map(int, input().split())
B = (M * 2) - A
print(B)