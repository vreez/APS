import sys; sys.stdin = open("2480.txt", "r")

arr = list(map(int, input().split()))
nums = list(set(arr))
length = len(nums)

if length == 1:
    print(10000 + (arr[0] * 1000))
elif length == 2:
    if arr.count(nums[0]) == 2:
        print(1000 + (nums[0] * 100))
    else:
        print(1000 + (nums[1] * 100))
else:
    print(max(arr) * 100)
