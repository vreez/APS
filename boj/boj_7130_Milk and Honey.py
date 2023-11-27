import sys; sys.stdin = open("7130.txt", "r")

M, H = map(int, input().split())
N = int(input())
total = 0
for i in range(N):
    C, B = map(int, input().split())
    if C * M >= B * H:
        total += (C * M)
    else:
        total += (B * H)

print(total)