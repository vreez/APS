import sys; sys.stdin = open("23803.txt", "r")

N = int(input())

for i in range(N*4):
    print("@"*N)
for j in range(N):
    print("@"*N*5)