import sys; sys.stdin = open("2742.txt", "r")

N = int(input())

for i in range(N, -1, -1):
    if i != 0:
        print(i)