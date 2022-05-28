import sys; sys.stdin = open("1546.txt", "r")

N = int(input())
arr = list(map(int, input().split()))

maxNum = max(arr)

total = 0
for i in range(N):
    newArr = arr[i] / maxNum * 100
    total += newArr

print(total / N)