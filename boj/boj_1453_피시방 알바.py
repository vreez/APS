import sys; sys.stdin = open("1453.txt", "r")

N = int(input())

arr = list(map(int, input().split()))

nums = [0] * 101

count = 0
for i in arr:
    if nums[i] != 0:
        count += 1
    else:
        nums[i] += 1

print(count)