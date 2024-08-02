import sys; sys.stdin = open("32046.txt", "r")

while True:
    n = int(input())
    if n == 0:
        break
    else:
        total = 0
        arr = list(map(int, input().split()))
        for i in range(n):
            if total + arr[i] <= 300:
                total += arr[i]
        print(total)
