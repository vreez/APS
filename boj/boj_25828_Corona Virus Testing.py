import sys; sys.stdin = open("25828.txt", "r")

g, p, t = map(int, input().split())
if g * p < (t * p) + g:
    print(1)
elif g * p > (t * p) + g:
    print(2)
else:
    print(0)