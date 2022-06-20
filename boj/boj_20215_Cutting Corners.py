import sys; sys.stdin = open("20215.txt", "r")

w, h = map(int, input().split())

d = (w**2 + h**2)**0.5
r = w + h

print(r - d)

