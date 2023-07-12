import sys; sys.stdin = open("26741.txt", "r")

x, y = map(int, input().split())

a = ((4*x) - y) // 2
b = x - a
print(a, b)