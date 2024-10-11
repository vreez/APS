import sys; sys.stdin = open("20205.txt", "r")

N, K = map(int, input().split())
res = []
for i in range(N):
    arr = list(input().split())
    for j in range(K):
        ans = ""
        for n in arr:
            ans += (n * K)
        res.append(ans)

for i in res:
    print(*i)