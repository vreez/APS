import sys; sys.stdin = open("4592.txt", "r")

while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1:
        break
    N = nums[0]
    arr = [0]
    for i in range(1, len(nums)):
        if nums[i] != arr[-1]:
            arr.append(nums[i])
    arr.append('$')
    arr.pop(0)

    for j in range(len(arr)):
        print(arr[j], end=" ")
    print()
