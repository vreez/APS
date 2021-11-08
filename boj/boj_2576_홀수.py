import sys; sys.stdin = open("2576.txt", "r")

nums = []
total = 0
for _ in range(7):
    num = int(input())
    if num % 2 != 0:
        total += num
        nums.append(num)

if total == 0:
    print(-1)
else:
    print(total)
    print(min(nums))