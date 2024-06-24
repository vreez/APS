import sys; sys.stdin = open("31962.txt", "r")

N, X = map(int, input().split())
ans = []
for i in range(N):
    S, T = map(int, input().split())
    if S + T <= X:
        ans.append(S)
new = sorted(ans)
if len(ans) > 0:
    print(new[-1])
else:
    print(-1)
