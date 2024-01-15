import sys; sys.stdin = open("21197.txt", "r")

N = int(input())
ans = 0
arr = []
if N % 2 == 0:
    for i in range(N):
        t = int(input())
        arr.append(t)
    for i in range(N):
        if i % 2 != 0:
            ans += (arr[i] - arr[i-1])
    print(ans)
else:
    print("still running")