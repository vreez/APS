import sys; sys.stdin = open("10188.txt", "r")

N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    for j in range(b):
        for k in range(a):
            print('X', end="")
        print()
    print()
            