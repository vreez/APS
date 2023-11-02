import sys; sys.stdin = open("29986.txt", "r")

N, H = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if arr[i] <= H:
        cnt += 1

print(cnt)