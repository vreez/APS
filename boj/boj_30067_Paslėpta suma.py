import sys; sys.stdin = open("30067.txt", "r")
arr = []
for i in range(10):
    num = int(input())
    arr.append(num)

total = sum(arr)
for i in range(10):
    if arr[i] == (total-arr[i]):
        print(arr[i])
        break
