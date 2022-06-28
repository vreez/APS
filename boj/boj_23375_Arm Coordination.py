import sys; sys.stdin = open("23375.txt", "r")

x, y = map(int, input().split())
r = int(input())

print(x - r, y + r)
print(x + r, y + r)
print(x + r, y - r)
print(x - r, y - r)