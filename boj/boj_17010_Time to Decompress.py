import sys; sys.stdin = open("17010.txt", "r")

L = int(input())
for i in range(L):
    N, x = input().split()
    print(int(N) * x)