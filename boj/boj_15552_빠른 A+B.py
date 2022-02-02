import sys; sys.stdin = open("15552.txt", "r")

N = int(sys.stdin.readline())

for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)