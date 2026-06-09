S, E = map(int, input().split())
K = int(input())
ans = []
for i in range(S, E-1, -K):
    ans.append(i)
print(*ans)