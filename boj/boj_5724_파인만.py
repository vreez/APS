import sys; sys.stdin = open("5724.txt", "r")

while True:
    N = int(input())
    if N == 0:
        break
    else:
        total = 0
        for i in range(1, N+1):
            total += i * i
        print(total)