import sys; sys.stdin = open("8558.txt", "r")

n = int(input())

if n <= 1:
    print(1)
else:
    result = 1
    for i in range(1, n + 1):
        result *= i
    answer = result % 10
    print(answer)