import sys; sys.stdin = open("2712.txt", "r")

N = int(input())
for i in range(N):
    arr = list(input().split())
    if arr[1] == "kg":
        print("{:.4f} lb".format(float(arr[0]) * 2.2046))
    elif arr[1] == "l":
        print("{:.4f} g".format(float(arr[0]) * 0.2642))
    elif arr[1] == "lb":
        print("{:.4f} kg".format(float(arr[0]) * 0.4536))
    else:
        print("{:.4f} l".format(float(arr[0]) * 3.7854))