import sys; sys.stdin = open("5063.txt", "r")

N = int(input())
for i in range(N):
    r, e, c = map(int, input().split())
    if r < e - c:
        print("advertise")
    elif r > e - c:
        print("do not advertise")
    else:
        print("does not matter")