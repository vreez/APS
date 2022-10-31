import sys; sys.stdin = open("10698.txt", "r")

N = int(input())
for i in range(N):
    arr = list(input().split())
    if arr[1] == "+":
        if int(arr[0]) + int(arr[2]) == int(arr[4]):
            print("Case {}: YES".format(i+1))
        else:
            print("Case {}: NO".format(i + 1))
    else:
        if int(arr[0]) - int(arr[2]) == int(arr[4]):
            print("Case {}: YES".format(i+1))
        else:
            print("Case {}: NO".format(i + 1))

