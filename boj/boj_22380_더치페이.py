import sys; sys.stdin = open("22380.txt", "r")

while True:
    N, M = map(int, input().split())
    total = 0
    if N == M and N == 0:
        break
    else:
        arr = list(map(int, input().split()))
        num = M // N
        for i in range(N):
            if arr[i] < num:
                total += arr[i]
            else:
                total += num
        print(total)

