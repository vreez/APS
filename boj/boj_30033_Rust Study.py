import sys; sys.stdin = open("30033.txt", "r")

N = int(input())
plan = list(map(int, input().split()))
do = list(map(int, input().split()))
ans = 0
for i in range(N):
    if plan[i] <= do[i]:
        ans += 1
print(ans)