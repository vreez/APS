import sys; sys.stdin = open("13118.txt", "r")

arr = list(map(int, input().split()))
x, y, r = map(int, input().split())

answer = 0
for i in range(len(arr)):
    if arr[i] == x:
        answer = (i + 1)

print(answer)