import sys; sys.stdin = open("15923.txt", "r")

N = int(input())
arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])
ans = 0
for i in range(N):
    if i < N-1:
        if arr[i][0] != arr[i+1][0]:
            ans += abs(arr[i][0] - arr[i+1][0])
        else:
            ans += abs(arr[i][1] - arr[i+1][1])
    else:
        if arr[i][0] != arr[0][0]:
            ans += abs(arr[i][0] - arr[0][0])
        else:
            ans += abs(arr[i][1] - arr[0][1])
print(ans)