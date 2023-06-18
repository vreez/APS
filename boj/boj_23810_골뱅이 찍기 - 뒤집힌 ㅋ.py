import sys; sys.stdin = open("23810.txt", "r")

N = int(input())
for i in range(5):
    if i % 2 == 0 and i != 4:
        for i in range(N):
            print("@"*N*5)
    else:
        for i in range(N):
            print("@"*N)
