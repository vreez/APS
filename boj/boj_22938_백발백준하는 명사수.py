import sys; sys.stdin = open("22938.txt", "r")

x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

dis = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
if r1 + r2 > dis:
    print("YES")
else:
    print("NO")