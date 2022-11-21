import sys; sys.stdin = open("26040.txt", "r")

arr = list(input())
alpha = list(input().split())

answer = ''
for i in range(len(arr)):
    if arr[i] in alpha:
        answer += arr[i].lower()
    else:
        answer += arr[i]

print(answer)