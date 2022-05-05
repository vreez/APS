import sys; sys.stdin = open("13136.txt", "r")

R, C, N = map(int, input().split())

A = R // N
if R % N != 0:
    A += 1


B = C // N
if C % N != 0:
    B += 1

print(A * B)