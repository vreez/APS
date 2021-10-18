import sys; sys.stdin = open("2752.txt", "r")

nums = list(map(int, input().split()))

result = sorted(nums)

for i in range(3):
    if i != 2:
        print(result[i], end=' ')
    else:
        print(result[i])