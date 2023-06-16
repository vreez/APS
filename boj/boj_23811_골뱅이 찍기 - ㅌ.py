import sys; sys.stdin = open("23811.txt", "r")

N = int(input())

for i in range(5):
    if i % 2 == 0:
        for j in range(N):
            print("@"*N*5)
    else:
        for j in range(N):
            print("@"*N)

