import sys; sys.stdin = open("11021.txt", "r")

N = int(input())

for i in range(N):
    A, B = map(int, input().split())
    print("Case #{}: {}".format(i + 1, A+B))