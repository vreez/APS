import sys; sys.stdin = open("2163.txt", "r")

N, M = map(int, input().split())

print(N * M - 1)