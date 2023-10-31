import sys; sys.stdin = open("29752.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
ans = []
cnt = 0
for i in range(N):
    if arr[i] != 0:
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 0
    ans.append(cnt)

print(max(ans))