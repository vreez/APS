import sys; sys.stdin = open("8760.txt", "r")

Z = int(input())

for i in range(Z):
    W, K = map(int, input().split())
    print(W * K // 2)

