import sys; sys.stdin = open("24072.txt", "r")

A, B, C = map(int, input().split())

if C >= A and C < B:
    print(1)
else:
    print(0)