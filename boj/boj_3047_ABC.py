import sys; sys.stdin = open("3047.txt", "r")

nums = list(map(int, input().split()))
arr = list(input())
new_nums = sorted(nums)
for i in arr:
    if i == 'A':
        print(new_nums[0], end=" ")
    elif i == 'B':
        print(new_nums[1], end=" ")
    else:
        print(new_nums[2], end=" ")
