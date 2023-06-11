import sys; sys.stdin = open("23804.txt", "r")

N = int(input())
for i in range(N):
    print("@"*N*5)
for i in range(N*3):
    print("@"*N)
for i in range(N):
    print("@"*N*5)