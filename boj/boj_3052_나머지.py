import sys; sys.stdin = open("3052.txt", "r")

nums = []
for i in range(10):
    nums.append(int(input()))
remainder = []

for i in range(10):
    if nums[i] % 42 not in remainder:
        remainder.append(nums[i] % 42)

print(len(remainder))