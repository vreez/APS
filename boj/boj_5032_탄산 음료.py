import sys; sys.stdin = open("5032.txt", "r")

e, f, c = map(int, input().split())
b = e + f
ans = 0
while b // c:
    ans += b // c
    b = b // c + b % c
print(ans)
