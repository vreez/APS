import sys; sys.stdin = open("24365.txt", "r")

A, B, C = map(int, input().split())

total = A + B + C
avg = total // 3
ma = avg - A
mc = C - avg
print(mc + ma)