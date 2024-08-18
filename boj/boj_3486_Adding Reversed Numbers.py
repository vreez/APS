import sys; sys.stdin = open("3486.txt", "r")

N = int(input())
for i in range(N):
    a, b = input().split()
    a, b = int(a[::-1]), int(b[::-1])
    total = int(str(a+b)[::-1])
    print(total)