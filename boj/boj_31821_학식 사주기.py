import sys; sys.stdin = open("31821.txt", "r")

ans = 0
N = int(input())
menu = []
for i in range(N):
    price = int(input())
    menu.append(price)
M = int(input())
for j in range(M):
    B = int(input())
    ans += menu[B-1]
print(ans)