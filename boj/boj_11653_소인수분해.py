import sys; sys.stdin = open("11653.txt", "r")

N = int(input())
if N != 1:
    for i in range(2, N+1):
        if N % i == 0:
            while N % i == 0:
                print(i)
                N = N / i