import sys; sys.stdin = open("16204.txt", "r")

N, M, K = map(int, input().split())

a = min(M, K)
b = min(N-M, N-K)
print(a+b)