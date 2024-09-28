import sys; sys.stdin = open("32141.txt", "r")

N, H = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if H > 0:
        H -= arr[i]
        cnt += 1
    else:
        break
if H > 0:
    print(-1)
else:
    print(cnt)

