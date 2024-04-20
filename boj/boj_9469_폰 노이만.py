import sys; sys.stdin = open("9469.txt", "r")

P = int(input())
for i in range(P):
    N, D, A, B, F = map(float, input().split())
    fly = F * (D / (A+B))
    print("{:.0f} {:.6f}".format(N, fly))