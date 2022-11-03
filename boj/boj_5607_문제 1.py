import sys; sys.stdin = open("5607.txt", "r")

N = int(input())
total_a = 0
total_b = 0
for i in range(N):
    a, b = map(int, input().split())
    if a > b:
        total_a += (a+b)
    elif a < b:
        total_b += (a+b)
    else:
        total_a += a
        total_b += b

print(total_a, total_b)