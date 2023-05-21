import sys; sys.stdin = open("26332.txt", "r")

N = int(input())
for i in range(N):
    f, s = map(int, input().split())
    total = (f * s) - ((f - 1)*2)
    print(f, s)
    print(total)