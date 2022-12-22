import sys; sys.stdin = open("6840.txt", "r")

nums = []
for i in range(3):
    n = int(input())
    nums.append(n)

new_nums = sorted(nums)
print(new_nums[1])