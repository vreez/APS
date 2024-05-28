import sys; sys.stdin = open("31868.txt", "r")
N, K = map(int, input().split())
ans = K
for i in range(N-1):
    ans = ans // 2
print(ans)