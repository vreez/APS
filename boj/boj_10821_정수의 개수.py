import sys; sys.stdin = open("10821.txt", "r")

nums = list(input())

print(nums.count(",") + 1)
