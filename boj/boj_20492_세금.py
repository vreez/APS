import sys; sys.stdin = open("20492.txt", "r")

N = int(input())

A = int(N * 0.78)
B = int(N - (N * 0.2 * 0.22))
print(A, B)
