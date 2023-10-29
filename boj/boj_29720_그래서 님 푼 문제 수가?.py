import sys; sys.stdin = open("29720.txt", "r")

N, M, K = map(int, input().split())

small = N - (M * K)
if small < 0:
    small = 0
big = N - (M * K) + M - 1
if big < 0:
    big = 0
print(small, big)