import sys; sys.stdin = open("9288.txt", "r")

T = int(input())
for i in range(T):
    print("Case {}:".format(i+1))
    N = int(input())
    for j in range(1, N//2+1):
        if (N - j) <= 6:
            print("({},{})".format(j, N-j))
