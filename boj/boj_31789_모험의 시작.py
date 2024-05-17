import sys; sys.stdin = open("31789.txt", "r")

flag = False
N = int(input())
x, s = map(int, input().split())
for i in range(N):
    c, p = map(int, input().split())
    if x >= c and p > s:
        flag = True
        break
if flag == True:
    print("YES")
else:
    print("NO")