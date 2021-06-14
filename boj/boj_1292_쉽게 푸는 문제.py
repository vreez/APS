import sys; sys.stdin = open("1292.txt", "r")

A, B = map(int, input().split())
arr = [0] * 1000

for i in range(1000):
    for j in range((i*(i+1)) // 2-i, (i*(i+1)) // 2):
        if j < 1000:
            arr[j] = i

total = 0
for i in range(A-1, B):
    total += arr[i]

print(total)


