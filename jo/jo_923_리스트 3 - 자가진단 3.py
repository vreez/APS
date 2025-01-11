import sys; sys.stdin = open("923.txt", "r")

arr = list(map(int, input().split()))
li = [0] * 10
for i in range(len(arr)):
    if arr[i] < 10:
        li[0] += 1
    else:
        li[arr[i] // 10] += 1
for i in range(len(li)):
    if li[i] != 0:
        print("{} : {}".format(i, li[i]))