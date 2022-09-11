import sys; sys.stdin = open("1598.txt", "r")

n, m = map(int, input().split())

n -= 1
m -= 1

a = n // 4
b = n % 4

c = m // 4
d = m % 4

answer = abs(a - c) + abs(b - d)

print(answer)

