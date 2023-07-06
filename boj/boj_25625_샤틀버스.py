import sys; sys.stdin = open("25625.txt", "r")

x, y = map(int, input().split())
if y > x:
    print(y-x)
elif x > y:
    print(x+y)
else:
    print(x)