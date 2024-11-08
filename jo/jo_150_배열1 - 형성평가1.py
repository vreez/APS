import sys; sys.stdin = open("150.txt", "r")

arr = list(input().split())
new = arr[::-1]
print(*new)