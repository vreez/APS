import sys; sys.stdin = open("30167.txt", "r")

ans = -1
l, r = map(int, input().split())
for i in range(l, r+1):
    if len(str(i)) == len(set(str(i))):
        ans = i
        break
print(ans)