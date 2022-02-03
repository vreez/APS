import sys; sys.stdin = open("2914.txt", "r")

A, I = map(int, input().split())
print(A * (I - 1) + 1)