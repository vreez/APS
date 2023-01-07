import sys; sys.stdin = open("25628.txt", "r")

A, B = map(int, input().split())

Bre = A // 2
Pat = B

if Bre <= Pat:
    print(Bre)
else:
    print(Pat)
