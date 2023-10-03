import sys; sys.stdin = open("30007.txt", "r")

N = int(input())
for i in range(N):
    a, b, x = map(int, input().split())
    ans = (a*(x-1))+b
    print(ans)