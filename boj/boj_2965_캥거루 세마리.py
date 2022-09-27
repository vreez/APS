import sys; sys.stdin = open("2965.txt", "r")

A, B, C = map(int, input().split())
D = max(B-A, C-B) - 1
print(D)