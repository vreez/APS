import sys; sys.stdin = open("28225.txt", "r")

n, f = map(int, input().split())
check = 10000000000
ans = 0
for i in range(n):
    x, v = map(int, input().split())
    result = (f - x) / v
    if result < check:
        check = result
        ans = i+1

print(ans)