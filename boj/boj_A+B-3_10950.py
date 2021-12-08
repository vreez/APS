import sys; sys.stdin = open("A+B-3.txt", "r")

N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    print(A+B)
