import sys; sys.stdin = open("25600.txt", "r")

N = int(input())
big = 0
for i in range(N):
    a, d, g = map(int, input().split())
    result = a * (d+g)
    if a == (d + g):
        result = result * 2
    if result > big:
        big = result

print(big)
        