import sys; sys.stdin = open("10989.txt", "r")

N = int(input())
arr = [0] * 10001
for _ in range(N):
    arr[int(input())] += 1

for i in range(10001):
    if arr[i] > 0:
        count = arr[i]
        while count > 0:
            print(i)
            count -= 1

