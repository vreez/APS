import sys; sys.stdin = open("5987.txt", "r")

T = int(input())
for i in range(T):
    N, C, S = input().split()

    for j in range(int(C)):
        S = S[int(N):] + S
    print(S)

