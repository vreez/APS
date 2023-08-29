import sys; sys.stdin = open("5176.txt", "r")

K = int(input())
for i in range(K):
    p, m = map(int, input().split())
    arr = [0] * (m+1)
    ans = 0
    for j in range(p):
        num = int(input())
        if arr[num] == 0:
            arr[num] = 1
            ans += 1
    print(p-ans)

