import sys; sys.stdin = open("5612.txt", "r")

n = int(input())
m = int(input())
total = [m]+[0] * (n)
for j in range(n):
    i, o = map(int, input().split())
    m += i
    m -= o
    if m < 0:
        break
    total[j+1] = m
if m < 0:
    print(0)
else:
    ans = 0
    check = True
    for k in range(len(total)):
        if check == True and total[k] == max(total):
            ans = total[k]
            check = False
    print(ans)