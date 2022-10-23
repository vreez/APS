import sys; sys.stdin = open("10599.txt", "r")

while True:
    arr = list(map(int, input().split()))
    if arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[3] and arr[0] == 0:
        break
    else:
        print(arr[2] - arr[1], arr[3] - arr[0])
        