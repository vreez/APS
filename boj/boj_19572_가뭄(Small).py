import sys; sys.stdin = open("19572.txt", "r")

d1, d2, d3 = map(int, input().split())
a = (d1 + d2 - d3) / 2
b = (d1 + d3 - d2) / 2
c = (d2 + d3 - d1) / 2

if a <= 0 or b <= 0 or c <= 0:
    print(-1)
else:
    print(1)
    print(a, b, c)