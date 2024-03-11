import sys; sys.stdin = open("7782.txt", "r")
n = int(input())
flag = False
b1, b2 = map(int, input().split())
for i in range(n):
    lx, ly, hx, hy = map(int, input().split())
    if (lx <= b1 and hx >= b1) and (ly <= b2 and hy >= b2):
        flag = True
if flag == True:
    print("Yes")
else:
    print("No")