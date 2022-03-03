import sys; sys.stdin = open("15964.txt", "r")

A, B = map(int, input().split())

print((A + B) * (A - B))