import sys; sys.stdin = open("21603.txt", "r")

N, K = map(int, input().split())

total = 0
nums = []
for i in range(1, N+1):
    if i % 10 != K % 10 and i % 10 != (2*K) % 10:
        total += 1
        nums.append(i)

print(total)
for j in range(len(nums)):
    print(nums[j], end=" ")