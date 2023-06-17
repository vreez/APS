import sys; sys.stdin = open("23812.txt", "r")

N = int(input())

for i in range(5):
    if i % 2 == 0:
        for j in range(N):
            print("@"*N+" "*N*3+"@"*N)
    else:
        for j in range(N):
            print("@"*N*5)