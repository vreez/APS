import sys; sys.stdin = open("25642.txt", "r")

A, B = map(int, input().split())
check = 0
while True:
    if A >= 5 or B >= 5:
        break
    else:
        if check == 0:
            B = A + B
            check = 1
        else:
            A = A + B
            check = 0

if A < B:
    print("yt")
else:
    print("yj")
