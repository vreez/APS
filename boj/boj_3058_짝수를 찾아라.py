import sys; sys.stdin = open("3058.txt", "r")

T = int(input())
for i in range(T):
    arr = list(map(int, input().split()))
    small = 101
    total = 0
    for j in range(len(arr)):
        if arr[j] % 2 == 0:
            total += arr[j]
            if arr[j] < small:
                small = arr[j]

    print(total, small)