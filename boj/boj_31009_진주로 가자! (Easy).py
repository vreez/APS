import sys; sys.stdin = open("31009.txt", "r")

N = int(input())
arr = []
jinju = 0
for i in range(N):
    D, C = input().split()
    arr.append(int(C))
    if D == "jinju":
        jinju = int(C)
ans = 0
for i in range(N):
    if arr[i] > jinju:
        ans += 1
print(jinju)
print(ans)