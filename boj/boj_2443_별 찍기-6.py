import sys; sys.stdin = open("2443.txt", "r")

N = int(input())

for i in range(N):
    print(" " * i + "*" * (2 * (N - i) - 1))