import sys; sys.stdin = open("11549.txt", "r")

T = int(input())
arr = list(map(int, input().split()))

answer = 0

for i in range(5):
    if arr[i] == T:
        answer += 1

print(answer)