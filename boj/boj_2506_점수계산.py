import sys; sys.stdin = open("2506.txt", "r")

N = int(input())
arr = list(map(int, input().split()))

total = 0
num = 1
for i in range(N):
    if arr[i] == 1:
        total += num
        num += 1
    else:
        num = 1

print(total)