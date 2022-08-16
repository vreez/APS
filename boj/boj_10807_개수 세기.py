import sys; sys.stdin = open("10807.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
V = int(input())

answer = 0
for i in range(N):
    if arr[i] == V:
        answer += 1

print(answer)