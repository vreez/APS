import sys; sys.stdin = open("15818.txt", "r")

N, M = map(int, input().split())
total = 1
arr = list(map(int, input().split()))
for i in range(N):
    total *= (arr[i] % M)
print(total % M)