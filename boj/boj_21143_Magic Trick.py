import sys; sys.stdin = open("21143.txt", "r")

s = list(input())
new = set(s)

if len(s) == len(new):
    print(1)
else:
    print(0)