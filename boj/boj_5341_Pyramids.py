import sys; sys.stdin = open("5341.txt", "r")

while True:
    N = int(input())
    if N == 0:
        break
    else:
        print(N*(N+1)//2)