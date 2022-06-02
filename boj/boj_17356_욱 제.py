import sys; sys.stdin = open("17356.txt", "r")

A, B = map(int, input().split())
M = (B - A) / 400
result = 1/(1 + 10 ** M)

print(result)