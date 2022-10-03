import sys; sys.stdin = open("9713.txt", "r")

T = int(input())
for i in range(T):
    N = int(input())
    total = 0
    for j in range(1, N+1):
        if j % 2:
            total += j
    print(total)        