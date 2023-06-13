import sys; sys.stdin = open("23806.txt", "r")

N = int(input())
for i in range(N):
    print("@"*N*5)
for i in range(N*3):
    print("@"*N+" "*N*3+"@"*N)
for i in range(N):
    print("@" * N * 5)