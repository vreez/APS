import sys
sys.stdin = open("1210.txt")


for t in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    n = 99
    m = 0
    for i in range(100):
        if arr[99][i] == 2:
            m = i

    while n != 0:
        if (arr[n][m] == 3 or arr[n - 1][m] == 3) and m > 0 and arr[n][m - 1] == 1:
            m -= 1
            arr[n][m] = 3
        elif (arr[n][m] == 3 or arr[n - 1][m] == 3) and m < 99 and arr[n][m + 1] == 1:
            m += 1
            arr[n][m] = 3
        else:
            n -= 1
            arr[n][m] = 3

    print("#{} {}".format(t, m))