import sys; sys.stdin = open("1534.txt", "r")

A, B = map(int, input().split(" "))

nums = ['A', 'B', 'C', 'D', 'E', 'F']

answer = ''

while A > 0:
    number = A % B
    if number >= 10:
        number = nums[number - 10]
    answer = str(number) + answer
    A = A // B
print(answer)

