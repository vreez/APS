import sys; sys.stdin = open("13222.txt", "r")

N, W, H = map(int, input().split())
D = ((W ** 2) + (H ** 2))**0.5
for i in range(N):
    num = int(input())
    if num <= W or num <= H or num <= D:
        print("YES")
    else:
        print("NO")