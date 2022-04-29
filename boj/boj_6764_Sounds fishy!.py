import sys; sys.stdin = open("6764.txt", "r")

nums = [int(input()) for _ in range(4)]
if nums[0] < nums[1] and nums[1] < nums[2] and nums[2] < nums[3]:
    print("Fish Rising")
elif nums[0] > nums[1] and nums[1] > nums[2] and nums[2] > nums[3]:
    print("Fish Diving")
elif max(nums) == min(nums):
    print("Fish At Constant Depth")
else:
    print("No Fish")