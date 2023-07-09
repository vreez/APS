import sys; sys.stdin = open("26933.txt", "r")

total = 0
N = int(input())
for i in range(N):
    H, B, K = map(int, input().split())
    if B > H:
        total += ((B-H)*K)

print(total)