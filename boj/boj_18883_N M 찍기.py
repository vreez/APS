import sys; sys.stdin = open("18883.txt", "r")

N, M = map(int, input().split())

num = 0
for i in range(N):
    for j in range(M):
        num += 1
        if j < M-1:
            print(num, end=" ")
        else:
            print(num, end="")
    print()