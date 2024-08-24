import sys;sys.stdin = open("1551.txt", "r")

N, K = map(int, input().split())
arr = list(map(int, input().split(",")))

while K > 0:
    new = []
    for i in range(len(arr)-1):
        new.append(arr[i+1]-arr[i])
    arr = new
    K -= 1

for i in range(len(arr)):
    if i != (len(arr)-1):
        print(arr[i], end=",")
    else:
        print(arr[i])