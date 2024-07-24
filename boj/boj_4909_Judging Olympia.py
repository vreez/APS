import sys; sys.stdin = open("4909.txt", "r")

while True:
    arr = list(map(int, input().split()))
    if max(arr) == 0 and min(arr) == 0:
        break
    else:
        total = sum(arr) - max(arr) - min(arr)
        if total % 4 == 0:
            print(total // 4)
        else:
            print(total/4)
