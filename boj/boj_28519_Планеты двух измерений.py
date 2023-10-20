import sys; sys.stdin = open("28519.txt", "r")

x, y = map(int, input().split())
if x != y:
    if x > y:
        print(y*2+1)
    else:
        print(x*2+1)
else:
    print(x+y)