import sys; sys.stdin = open("16479.txt", "r")

K = int(input())
D1, D2 = map(int, input().split())

answer = (K**2) - (((D1 - D2) / 2)**2)
print(answer)