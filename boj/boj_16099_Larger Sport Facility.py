import sys; sys.stdin = open("16099.txt", "r")

n = int(input())
for i in range(n):
    lt, wt, le, we = map(int, input().split())
    T = lt * wt
    E = le * we
    if T > E:
        print("TelecomParisTech")
    elif E > T:
        print("Eurecom")
    else:
        print("Tie")