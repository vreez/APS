import sys; sys.stdin = open("2979.txt", "r")

A, B, C = map(int, input().split())
time = [0] * 101

for _ in range(3):
    arr, lev = map(int, input().split())
    for i in range(arr, lev):
        time[i] += 1
total = 0
for i in range(101):
    if time[i] == 1:
        total += (1*A)
    elif time[i] == 2:
        total += (2*B)
    elif time[i] == 3:
        total += (3*C)

print(total)