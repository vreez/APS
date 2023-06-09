import sys; sys.stdin = open("23802.txt", "r")

N = int(input())
for _ in range(N):
    print("@"*(N*5))
for _ in range(N*4):
    print("@"*N)