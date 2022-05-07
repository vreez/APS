import sys; sys.stdin = open("6810.txt", "r")

nums = [9,7,8,0,9,2,1,4,1,8]

e = nums.append(int(input()))
n = nums.append(int(input()))
t = nums.append(int(input()))

total = 0
for i in range(len(nums)):
    if i % 2 == 0:
        total += (nums[i] * 1)
    else:
        total += (nums[i] * 3)

print("The 1-3-sum is {}".format(total))
