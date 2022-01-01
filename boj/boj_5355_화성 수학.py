import sys; sys.stdin = open("5355.txt", "r")

N = int(input())
for _ in range(N):
    arr = list(input().split())
    num = float(arr[0])

    for i in range(1, len(arr)):
        if arr[i] == '@':
            num *= 3
        elif arr[i] == '%':
            num += 5
        else:
            num -= 7

    print('{:.2f}'.format(round(num, 2)))