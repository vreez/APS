import sys; sys.stdin = open("21633.txt", "r")

k = int(input())

total = k * 0.01 + 25
total = max(total, 100)
total = min(total, 2000)

print(total)