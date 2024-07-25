import sys; sys.stdin = open("4619.txt", "r")

while True:
    B, N = map(int, input().split())
    if B == N and B == 0:
        break
    else:
        i = 0
        while i**N <= B:
            i += 1
        if i**N-B < B-(i-1)**N:
            print(i)
        else:
            print(i-1)