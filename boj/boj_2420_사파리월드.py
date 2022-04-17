import sys; sys.stdin = open("2420.txt", "r")

N, M = map(int, input().split())

print(abs(N-M))