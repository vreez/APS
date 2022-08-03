import sys; sys.stdin = open("7891.txt", "r")

t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    print(x + y)