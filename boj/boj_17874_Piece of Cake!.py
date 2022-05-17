import sys; sys.stdin = open("17874.txt", "r")

n, h, v = map(int, input().split())

answer = max(n-h, h) * max(n-v, v) * 4
print(answer)