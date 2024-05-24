import sys; sys.stdin = open("31833.txt", "r")

N = int(input())
A = list(input().split())
B = list(input().split())

A = ''.join(A)
B = ''.join(B)

if int(A) <= int(B):
    print(int(A))
else:
    print(int(B))