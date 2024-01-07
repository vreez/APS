import sys; sys.stdin = open("14782.txt", "r")

N = int(input())
i = 2
nums = [0] * 1000000
while i <= N:
    if N % i == 0:
        nums[i] += 1
        N = N / i
    else:
        i += 1

ans = 1
for a in range(len(nums)):
    total = 0
    if nums[a] != 0:
        for b in range(nums[a]+1):
            total += (a**b)
        ans *= total

print(ans)