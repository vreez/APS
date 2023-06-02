import sys; sys.stdin = open("11772.txt", "r")

N = int(input())
total = 0
for i in range(N):
    num = int(input())
    origin = num // 10
    exponent = num % 10
    total += origin ** exponent

print(total)