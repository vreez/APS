import sys; sys.stdin = open("26545.txt", "r")

N = int(input())
total = 0
for i in range(N):
    total += int(input())

print(total)    