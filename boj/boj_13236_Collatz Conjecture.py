import sys; sys.stdin = open("13236.txt", "r")

N = int(input())
print(N, end=" ")
while N != 1:
    if N % 2 == 0:
        N = N // 2
        print(N, end=" ")
    else:
        N = N * 3 + 1
        print(N, end=" ")