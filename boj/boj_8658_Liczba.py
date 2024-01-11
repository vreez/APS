import sys; sys.stdin = open("8658.txt", "r")

n = int(input())
small = 0
big = 0
for i in range(2, n):
    if n % i != 0:
        small = i
        break
for j in range(n-1, 1, -1):
    if n % j != 0:
        big = j
        break
print(i, j)