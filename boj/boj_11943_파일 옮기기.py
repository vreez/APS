import sys; sys.stdin = open("11943.txt", "r")

A, B = map(int, input().split())
C, D = map(int, input().split())

print(min(A + D, B + C))