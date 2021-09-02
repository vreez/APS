import sys; sys.stdin = open("15815.txt", "r")
expression = list(input())
num = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
        ]
numbers = []
exp = []
for i in range(len(expression)):
    if expression[i] in num:
        numbers.append(int(expression[i]))
    else:
        if expression[i] == '+':
            numbers.append(numbers.pop() + numbers.pop())
        elif expression[i] == '-':
            first = numbers.pop()
            second = numbers.pop()
            numbers.append(second - first)
        elif expression[i] == '*':
            numbers.append(numbers.pop() * numbers.pop())
        elif expression[i] == '/':
            first = numbers.pop()
            second = numbers.pop()
            numbers.append(second // first)
print(numbers[0])