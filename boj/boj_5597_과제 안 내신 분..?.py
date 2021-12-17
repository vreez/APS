import sys; sys.stdin =open("5597.txt", "r")

nums = []

for i in range(28):
    nums.append(int(input()))

answer = []
for i in range(1, 31):
    if i not in nums:
        answer.append(i)

print(min(answer))
print(max(answer))