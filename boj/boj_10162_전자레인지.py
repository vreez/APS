import sys; sys.stdin = open("10162.txt", "r")

seconds = [300, 60, 10]
arr = [0, 0, 0]
N = int(input())
if N % 10:
    print(-1)
else:
    for i in range(3):
        arr[i] = N // seconds[i]
        N -= (arr[i] * seconds[i])

    for i in range(3):
        print(arr[i], end=" ")



