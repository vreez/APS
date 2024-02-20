import sys; sys.stdin = open("28808.txt", "r")

ans = 0
n, m = map(int, input().split())
for i in range(n):
    arr = list(input())
    if '+' in arr:
        ans += 1

print(ans)