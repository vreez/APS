import sys; sys.stdin = open("15036.txt", "r")

N = int(input())
arr = list(map(int, input().split()))

total = 0
for i in range(N):
    if arr[i] == 0:
        total += 2
    elif arr[i] == 1:
        total += 1
    elif arr[i] == 2:
        total += 0.5
    elif arr[i] == 4:
        total += 0.25
    elif arr[i] == 8:
        total += 0.125
    elif arr[i] == 16:
        total += 0.0625

print(total)