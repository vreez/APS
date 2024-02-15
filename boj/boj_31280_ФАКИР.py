import sys; sys.stdin = open("31280.txt", "r")

arr = list(map(int, input().split()))
new = sorted(arr, reverse=True)[:-1]
ans = sum(new) + 1
print(ans)
