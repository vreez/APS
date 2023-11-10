import sys; sys.stdin = open("30329.txt", "r")

arr = list(input())
cnt = 0
for i in range(len(arr)):
    if arr[i] == "k":
        ans = "".join(arr[i:i+4])
        if ans == "kick":
            cnt += 1

print(cnt)
