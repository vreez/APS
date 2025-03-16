import sys; sys.stdin = open("754.txt", "r")

mh = int(input())
mw = int(input())
kh = int(input())
kw = int(input())

if mh > kh and mw > kw:
    print(True)
else:
    print(False)