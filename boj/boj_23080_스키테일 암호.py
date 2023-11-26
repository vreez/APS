import sys; sys.stdin = open("23080.txt", "r")

K = int(input())
arr = list(input())
ans = ""
for i in range(0, len(arr), K):
    ans += arr[i]
print(ans)