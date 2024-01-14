import sys; sys.stdin = open("8574.txt", "r")

n, k, x, y = map(int, input().split())
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    if abs(x-a)**2 + abs(y-b)**2 > k**2:
        ans += 1
print(ans)