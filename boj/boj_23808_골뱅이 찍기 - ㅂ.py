import sys; sys.stdin = open("23808.txt", "r")

N = int(input())
for i in range(N*2):
    print("@"*N+" "*3*N+"@"*N)
for i in range(N):
    print("@"*N*5)
for i in range(N):
    print("@"*N+" "*3*N+"@"*N)
for i in range(N):
    print("@"*N*5)