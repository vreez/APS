import sys; sys.stdin = open("766.txt", "r")

words = list(input().split())
new = words[::-1]
print(*new)
