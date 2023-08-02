import sys; sys.stdin = open("28214.txt", "r")

N, K, P = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
for i in range(0, N*K, K):
    cnt = 0
    for j in range(K):
        if arr[i+j] == 0:
            cnt += 1
    if cnt < P:
        ans += 1

print(ans)