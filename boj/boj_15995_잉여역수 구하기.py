import sys; sys.stdin = open("15995.txt", "r")

a, m = map(int, input().split())
for i in range(1, 10001):
    if a * i % m == 1:
        print(i)
        break