import sys; sys.stdin = open("15963.txt", "r")

N, M = map(int, input().split())

if N == M:
    print(1)
else:
    print(0)