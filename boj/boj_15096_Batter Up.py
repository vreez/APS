import sys; sys.stdin = open("15096.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
total = 0
cnt = 0
for i in range(N):
    if arr[i] >= 0:
        total += arr[i]
        cnt += 1
ans = total / cnt
print(ans)