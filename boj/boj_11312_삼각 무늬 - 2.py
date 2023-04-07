import sys; sys.stdin = open("11312.txt", "r")

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(A//B * A//B)