S, E = map(int, input().split())
ans = []
if S > E:
    for i in range(E, S+1):
        ans.append(i)
else:
    for i in range(S, E+1):
        ans.append(i)
print(*ans)