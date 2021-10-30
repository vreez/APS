import sys; sys.stdin = open("1071.txt", "r")

N = int(input())
nums = list(map(int, input().split()))
M = int(input())

small = 0
large = 0
for i in range(N):
    if nums[i] < M:
        if M % nums[i] == 0:
            small += nums[i]
    elif nums[i] == M:
        small += nums[i]
        large += nums[i]
    else:
        if nums[i] % M == 0:
            large += nums[i]

print(small)
print(large)