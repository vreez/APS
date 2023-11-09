import sys; sys.stdin = open("13416.txt", "r")
T = int(input())
for _ in range(T):
    total = 0
    N = int(input())
    for i in range(N):
        arr = list(map(int, input().split()))
        if max(arr) > 0:
            total += max(arr)

    print(total)