import sys; sys.stdin = open("18406.txt", "r")

nums = list(map(int, input()))
length = len(nums)

A = sum(nums[:length // 2])
B = sum(nums[length // 2:])

if A == B:
    print("LUCKY")
else:
    print("READY")

