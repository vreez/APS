import sys; sys.stdin = open("20528.txt", "r")

N = int(input())
arr = list(input().split())
ans = []
for i in range(N):
    if arr[i][0] not in ans:
        ans.append(arr[i][0])
if len(ans) == 1:
    print(1)
else:
    print(0)