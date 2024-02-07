import sys; sys.stdin = open("28648.txt", "r")
N = int(input())
ans = []
for i in range(N):
    t, l = map(int, input().split())
    s = t + l
    ans.append(s)
print(min(ans))