import sys; sys.stdin = open("15780.txt", "r")

N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(K):
    if arr[i] % 2 == 0:
        cnt += (arr[i] // 2)
    else:
        cnt += (arr[i] // 2 + 1)
if cnt >= N:
    print("YES")
else:
    print("NO")