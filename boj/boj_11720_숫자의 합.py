import sys; sys.stdin = open("11720.txt", "r")

N = int(input())
numbers = list(input())

total = 0
for i in range(N):
    total += int(numbers[i])

print(total)
