import sys; sys.stdin = open("1731.txt", "r")

N = int(input())
arr = []
for i in range(N):
    num = int(input())
    arr.append(num)

if arr[1] - arr[0] == arr[2] - arr[1]:
    print(arr[-1] + (arr[1] - arr[0]))
else:
    print(arr[-1] * (arr[1] // arr[0]))
