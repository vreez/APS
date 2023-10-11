import sys; sys.stdin = open("29807.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
if N < 5:
    for i in range(5-N):
        arr.append(0)
if arr[0] > arr[2]:
    first = (arr[0] - arr[2]) * 508
else:
    first = (arr[2] - arr[0]) * 108
if arr[1] > arr[3]:
    second = (arr[1] - arr[3]) * 212
else:
    second = (arr[3] - arr[1]) * 305
third = arr[4] * 707

ans = (first + second + third) * 4763

print(ans)