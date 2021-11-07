import sys; sys.stdin = open("2577.txt", "r")

A = int(input())
B = int(input())
C = int(input())

result = A * B * C
result = list(str(result))

nums = {
    '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0,
    '6': 0, '7': 0, '8': 0, '9': 0
    }

for i in range(len(result)):
    nums[result[i]] += 1

for key, value in sorted(nums.items()):
    print(value)
