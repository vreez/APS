import sys; sys.stdin = open("2562.txt", "r")

maxNum = 0
answer = 0
for i in range(9):
    num = int(input())
    if num > maxNum:
        maxNum = num
        answer = i + 1

print(maxNum)
print(answer)