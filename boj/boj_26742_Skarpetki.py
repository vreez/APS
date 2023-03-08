import sys; sys.stdin = open("26742.txt", "r")

arr = list(input())

B = 0
C = 0
for i in range(len(arr)):
    if arr[i] == 'B':
        B += 1
    else:
        C += 1

ans = (B // 2) + (C // 2)
print(ans)
