import sys; sys.stdin = open("3046.txt", "r")

R1, S = map(int, input().split())

print(S*2 - R1)