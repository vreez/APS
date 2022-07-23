import sys; sys.stdin = open("8674.txt", "r")

a, b = map(int, input().split())

first = abs((a // 2) * b - (a - (a // 2)) * b)
second = abs((b // 2) * a - (b - (b // 2)) * a)

answer = min(first, second)

print(answer)