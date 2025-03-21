import sys; sys.stdin = open("767.txt", "r")

nums = list(map(int, input().split()))
print(((nums[0] + nums[1]) * nums[2]) / 2)