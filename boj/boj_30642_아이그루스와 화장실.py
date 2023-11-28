import sys; sys.stdin = open("30642.txt", "r")

N = int(input())
m = input()
K = int(input())

if m == "annyong":
    if K % 2 == 0:
        if K == N:
            print(K - 1)
        else:
            print(K + 1)
    else:
        print(K)
else:
    if K % 2 == 0:
        print(K)
    else:
        if K == N:
            print(K - 1)
        else:
            print(K + 1)
