import sys; sys.stdin = open("17548.txt", "r")

arr = list(input())

answer = ''
for i in range(len(arr)):
    if arr[i] == 'e':
        answer += 'ee'
    else:
        answer += arr[i]

print(answer)