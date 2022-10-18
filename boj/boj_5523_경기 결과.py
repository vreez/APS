import sys; sys.stdin = open("5523.txt", "r")

N = int(input())
aScore = 0
bScore = 0
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        aScore += 1
    elif b > a:
        bScore += 1

print(aScore, bScore)
