import sys; sys.stdin = open("15059.txt", "r")

arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

total = 0
if arr[0] <= arr2[0]:
    total += arr2[0] - arr[0]

if arr[1] <= arr2[1]:
    total += arr2[1] - arr[1]

if arr[2] <= arr2[2]:
    total += arr2[2] - arr[2]

print(total)