import sys; sys.stdin = open("31831.txt", "r")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
stress = 0
ans = 0
for i in range(N):
    stress += arr[i]
    if stress < 0:
        stress = 0
    if stress >= M:
        ans += 1
print(ans)