import sys; sys.stdin = open("26594.txt", "r")

arr = list(input())
i = 1
cnt = 1
for i in range(1, len(arr)):
    if arr[i] != arr[0]:
        break
    else:
        i += 1
        cnt += 1

print(cnt)
