import sys; sys.stdin = open("30876.txt", "r")

N = int(input())
check = 10000
ans1 = 0
ans2 = 0
for i in range(N):
    x, y = map(int, input().split())
    if check > y:
        ans1 = x
        ans2 = y
        check = y
print(ans1, ans2)