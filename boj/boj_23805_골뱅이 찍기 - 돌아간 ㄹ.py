import sys; sys.stdin = open("23805.txt", "r")

N = int(input())

for i in range(N):
    print("@"*3*N+" "*N+"@"*N)
for i in range(N*3):
    print("@"*N+" "*N+"@"*N+" "*N+"@"*N)
for i in range(N):
    print("@" * N + " " * N + "@" * 3 * N)