import sys; sys.stdin = open("30031.txt", "r")

N = int(input())
total = 0
for i in range(N):
    a, b = map(int, input().split())
    if a == 136:
        total += 1000
    elif a == 142:
        total += 5000
    elif a == 148:
        total += 10000
    elif a == 154:
        total += 50000
print(total)