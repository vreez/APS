import sys; sys.stdin = open("27434.txt", "r")

N = int(input())

total = 1
for i in range(1, N+1):
    total *= i
print(total)