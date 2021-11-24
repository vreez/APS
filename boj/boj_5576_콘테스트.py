import sys; sys.stdin = open("5576.txt", "r")

nums = []
for _ in range(20):
    nums.append(int(input()))

W = sorted(nums[:10])
K = sorted(nums[10:])

print(sum(W[-3:]), sum(K[-3:]))