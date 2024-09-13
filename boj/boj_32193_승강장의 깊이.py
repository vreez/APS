import sys; sys.stdin = open("32193.txt", "r")

N = int(sys.stdin.readline())
total = 0
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    total = A - B + total
    print(total)