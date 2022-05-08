import sys; sys.stdin = open("13866.txt", "r")

A, B, C, D = map(int, input().split())

first = B + C
second = A + D

if first > second:
    print(first - second)
else:
    print(second - first)


