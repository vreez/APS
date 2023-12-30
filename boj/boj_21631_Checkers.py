import sys; sys.stdin = open("21631.txt", "r")

a, b = map(int, input().split())
if a >= b:
    print(b)
else:
    print(a+1)