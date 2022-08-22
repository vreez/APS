import sys; sys.stdin = open("9325.txt", "r")

T = int(input())
for i in range(T):
    s = int(input())
    n = int(input())
    for j in range(n):
        q, p = map(int, input().split())
        s += (q * p)
    print(s)