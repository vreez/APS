import sys; sys.stdin = open("10610.txt", "r")

numbers = list(input())
numbers.sort(reverse=True)
result = -1

if numbers[-1] != '0':
    result = -1
else:
    total = 0
    for i in range(len(numbers) - 1):
        total += int(numbers[i])
    if total % 3 == 0:
        answer = ''.join(numbers)
        result = int(answer)
print(result)



