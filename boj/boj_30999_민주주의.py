import sys; sys.stdin = open("30999.txt", "r")

N, M = map(int, input().split())
ans = 0
op = []
for i in range(N):
    arr = list(input())
    op.append(arr)

for i in range(N):
    cnt = 0
    for j in range(M):
        if op[i][j] == "O":
            cnt += 1
    if cnt > M // 2:
        ans += 1
print(ans)
