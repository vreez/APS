import sys; sys.stdin = open("1977.txt", "r")

M = int(input())
N = int(input())
ans = []
for i in range(M, N+1):
    if int(i ** 0.5) ** 2 == i:
        ans.append(i)
if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(ans[0])