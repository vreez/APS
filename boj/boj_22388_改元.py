import sys; sys.stdin = open("22388.txt", "r")

while True:
    arr = list(input().split())
    if len(arr) == 1 and arr[0] == "#":
        break
    else:
        if int(arr[1]) > 31 or (int(arr[1]) == 31 and int(arr[2]) >= 5):
            print("{} {} {} {}".format("?", int(arr[1])-30, arr[2], arr[3]))
        else:
            print("{} {} {} {}".format(arr[0], arr[1], arr[2], arr[3]))