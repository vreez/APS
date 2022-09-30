import sys; sys.stdin = open("2783.txt", "r")

x, y = map(int, input().split())
op = x / y * 1000

n = int(input())
for i in range(n):
    xi, yi = map(int, input().split())
    np = xi / yi * 1000
    if np < op:
        op = np
op = format(op, ".2f")
print(op)