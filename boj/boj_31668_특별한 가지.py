import sys; sys.stdin = open("31668.txt", "r")

N = int(input())
M = int(input())
K = int(input())

ans = M // N * K
print(ans)