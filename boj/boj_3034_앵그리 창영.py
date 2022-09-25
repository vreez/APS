import sys; sys.stdin = open("3034.txt", "r")

N, W, H = map(int, input().split())

for i in range(N):
    M = int(input())
    if M <= W or M <= H or M <= (((W**2)+(H**2))**0.5):
        print("DA")
    else:
        print("NE")