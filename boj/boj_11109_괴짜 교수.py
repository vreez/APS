import sys; sys.stdin = open("11109.txt", "r")

T = int(input())
for i in range(T):
    d, n, s, p = map(int, input().split())
    if ((n * p) + d) > (n * s):
        print("do not parallelize")
    elif ((n * p) + d) < (n * s):
        print("parallelize")
    else:
        print("does not matter")