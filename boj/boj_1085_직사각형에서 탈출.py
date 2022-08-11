import sys; sys.stdin = open("1085.txt", "r")

x, y, w, h = map(int, input().split())

answer = min(abs(x-w), abs(y-h), x, y)
print(answer)