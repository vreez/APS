import sys; sys.stdin = open("30791.txt", "r")

arr = list(map(int, input().split()))
sixteen = arr[0]
cnt = 0
for i in arr[1:]:
    if sixteen - i <= 1000:
        cnt += 1

print(cnt)

