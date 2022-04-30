import sys; sys.stdin = open("2530.txt", "r")

A, B, C = map(int, input().split())
second = int(input())

total = (A * 3600) + (B * 60) + C + second

H = total // 3600
M = (total - H * 3600) // 60
S = (total - H * 3600) % 60

if H >= 24:
    H = H % 24

print(H, M, S)