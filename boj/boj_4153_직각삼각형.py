import sys; sys.stdin = open("4153.txt", "r")

while True:
    arr = list(map(int, input().split()))

    if arr[0] == arr[1] and arr[1] == arr[2] and arr[0] == 0:
        break
    else:
        if arr[0] == max(arr):
            if (arr[0] ** 2) == ((arr[1] ** 2) + (arr[2] ** 2)):
                print("right")
            else:
                print("wrong")
        elif arr[1] == max(arr):
            if (arr[1] ** 2) == ((arr[0] ** 2) + (arr[2] ** 2)):
                print("right")
            else:
                print("wrong")
        elif arr[2] == max(arr):
            if (arr[2] ** 2) == ((arr[0] ** 2) + (arr[1] ** 2)):
                print("right")
            else:
                print("wrong")
