import sys; sys.stdin  = open("6845.txt", "r")

N = int(input())
for i in range(N):
    y, m, d = map(int, input().split())
    if 2007 - y > 18:
        print("Yes")
    elif 2007 - y == 18:
        if 2 - m > 0:
            print("Yes")
        elif 2 - m == 0:
            if 27 - d >= 0:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")