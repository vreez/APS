import sys; sys.stdin = open("24860.txt", "r")

v1, j1 = map(int, input().split())
v2, j2 = map(int, input().split())
v, d, j = map(int, input().split())

print((v * d * j) * (v1 * j1 + v2 * j2))
