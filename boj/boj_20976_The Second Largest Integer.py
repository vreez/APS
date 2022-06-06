import sys; sys.stdin = open("20976.txt", "r")

nums = list(map(int, input().split()))
nums = sorted(nums)

print(nums[1])