import sys; sys.stdin = open("1284.txt", "r")

while True:
    nums = list(map(int, input()))
    if len(nums) == 1 and nums[0] == 0:
        break
    else:
        answer = 2
        answer += (len(nums) - 1)
        for i in range(len(nums)):
            if nums[i] == 1:
                answer += 2
            elif nums[i] == 0:
                answer += 4
            else:
                answer += 3

        print(answer)