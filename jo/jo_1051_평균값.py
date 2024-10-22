import sys; sys.stdin = open("1051.txt", "r")

R1, S = map(int, input().split())
R2 = (S * 2) - R1
print(R2)