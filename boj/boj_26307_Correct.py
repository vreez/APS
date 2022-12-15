import sys; sys.stdin = open("26307.txt", "r")

H, M = map(int, input().split())

print(((H-9) * 60) + M)