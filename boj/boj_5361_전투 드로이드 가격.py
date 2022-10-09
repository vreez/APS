import sys; sys.stdin = open("5361.txt", "r")

N = int(input())
for i in range(N):
    total = 0
    A, B, C, D, E = map(int, input().split())
    total += A * 350.34
    total += B * 230.90
    total += C * 190.55
    total += D * 125.30
    total += E * 180.90

    print("${:.2f}".format(total))
    