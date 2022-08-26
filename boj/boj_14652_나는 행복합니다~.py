import sys; sys.stdin = open("14652.txt", "r")

N, M, K = map(int, input().split())

a = K // M
b = K % M

print(a, b)
