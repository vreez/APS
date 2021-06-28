import sys; sys.stdin = open("input/3273.txt", "r")

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

check = []
count = 0
for i in range(n):
    picked = arr[i]
    arr[i] = -1
    if picked not in check and x-picked > 0 and x-picked in arr:
        count += 1
        check.append(picked)
        check.append(x-picked)

print(count)
