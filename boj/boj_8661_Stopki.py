import sys; sys.stdin = open("8661.txt", "r")

x, k, a = map(int, sys.stdin.readline().split())
check = 1
while True:
    if x < 0:
        if check == 0:
            print(1)
        else:
            print(0)
        break
    else:
        if check == 1:
            x -= k
            check = 0
        else:
            x -= a
            check = 1

